from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
import requests
from .models import FinancialOptions, FinancialProducts
from .serializers import FinancialOptionsSerializer, FinancialProductsSerializer

API_KEY = settings.API_KEY
URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def save_financial_products(request):
    response = requests.get(URL).json()
    products = response['result']['baseList']
    options = response['result']['optionList']

    for product in products:
        fin_prdt_cd = product.get('fin_prdt_cd')
        if FinancialProducts.objects.filter(fin_prdt_cd=fin_prdt_cd ).exists():
            continue

        serializer = FinancialProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for option in options:
        product = option.get('product')
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate') if option.get('intr_rate') is not None else -1
        intr_rate2 = option.get('intr_rate2') if option.get('intr_rate2') is not None else -1
        save_trm = option.get('save_trm')

        deposit_product = FinancialProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
       
        if FinancialOptions.objects.filter(product=deposit_product.id, 
                                        intr_rate_type_nm=intr_rate_type_nm, 
                                        intr_rate=intr_rate,
                                        intr_rate2=intr_rate2).exists():
            continue

        save_data = {
            'product' : deposit_product.id,
            'fin_prdt_cd': deposit_product.fin_prdt_cd, 
            'intr_rate_type_nm':intr_rate_type_nm, 
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2, 
            'save_trm':save_trm
        }

        serializer = FinancialOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    return JsonResponse({'message' : '저장 성공'})