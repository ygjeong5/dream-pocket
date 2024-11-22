from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Max, F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.http import JsonResponse
import requests
from .models import FinancialOptions, FinancialProducts, SavingOptions, SavingProducts
from .serializers import FinancialOptionsSerializer, FinancialProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer

API_KEY = settings.API_KEY
API_KEY_EXCHANGE = settings.API_KEY_EXCHANGE
URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
SAVING_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

# 금융 상품 API 데이터 저장
@api_view(['GET'])
@permission_classes([AllowAny])
def save_financial_products(request):
    # 예금 상품 저장
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
    # 적금 상품 저장
    response = requests.get(SAVING_API_URL).json()
    products = response['result']['baseList']
    options = response['result']['optionList']

    for product in products:
        fin_prdt_cd = product.get('fin_prdt_cd')
        if SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue

        serializer = SavingProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in options:
        fin_prdt_cd = option.get('fin_prdt_cd')
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'product': product.id,
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate') or -1,
            'intr_rate2': option.get('intr_rate2') or -1,
            'save_trm': option.get('save_trm')
        }

        if SavingOptions.objects.filter(**save_data).exists():
            continue

        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    return JsonResponse({'message' : '저장 성공', 'response':response})


@api_view(['GET'])
def exchange_rate(reaquest):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': API_KEY_EXCHANGE,
        'data': 'AP01',
    }
    response = requests.get(url, params=params, verify=False)
    return Response(response.json())


@api_view(['GET'])
def financial_product_detail(request, product_pk):
    product = FinancialProducts.objects.get(pk=product_pk)
    options = FinancialOptions.objects.filter(product=product_pk)
    product_serializer = FinancialProductsSerializer(product)
    option_serializer = FinancialOptionsSerializer(options, many=True)

    serializer = {
        "product" : product_serializer.data,
       "options" : option_serializer.data
    }

    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def financial_products_list(request):
    """
    금융 상품 리스트 검색, 정렬 및 기간 필터링
    """
    # GET 파라미터 가져오기
    bank_name = request.query_params.get('kor_co_nm', None)  # 은행 이름
    sort_by = request.query_params.get('sort', 'id')  # 정렬 기준
    min_term = request.query_params.get('min_term', None)  # 최소 기간
    max_term = request.query_params.get('max_term', None)  # 최대 기간

    # 금융 상품 쿼리셋 초기화
    products = FinancialProducts.objects.all()

    # 은행 이름 필터링
    if bank_name:
        products = products.filter(kor_co_nm__icontains=bank_name)

    # 기간 필터링 (FinancialOptions에서 연결된 기간 기준으로 필터링)
    if min_term or max_term:
        options = FinancialOptions.objects.all()
        if min_term:
            options = options.filter(save_trm__gte=int(min_term))
        if max_term:
            options = options.filter(save_trm__lte=int(max_term))
        product_ids = options.values_list('product_id', flat=True)
        products = products.filter(id__in=product_ids)

    # 정렬
    if sort_by == 'highest_rate':
        products = (
            products.annotate(max_rate=Max('financialoptions__intr_rate2'))
            .order_by('-max_rate')
        )

    # 데이터 직렬화
    serializer = FinancialProductsSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 적금 상품 리스트 가져오기 (정렬 기능 추가)
@api_view(['GET'])
@permission_classes([AllowAny])
def saving_products_list(request):
    bank_name = request.query_params.get('kor_co_nm', None)  # 은행 이름
    sort = request.query_params.get('sort', None)
    min_term = request.query_params.get('min_term', None)  # 최소 기간
    max_term = request.query_params.get('max_term', None)  # 최대 기간

    products = SavingProducts.objects.all()

    if bank_name:
        products = products.filter(kor_co_nm__icontains=bank_name)

    # 기간 필터링 (FinancialOptions에서 연결된 기간 기준으로 필터링)
    if min_term or max_term:
        options = SavingOptions.objects.all()
        if min_term:
            options = options.filter(save_trm__gte=int(min_term))
        if max_term:
            options = options.filter(save_trm__lte=int(max_term))
        product_ids = options.values_list('product_id', flat=True)
        products = products.filter(id__in=product_ids)

    if sort == 'highest_rate':
        # 최고 금리(intr_rate2 기준)로 내림차순 정렬
        products = SavingProducts.objects.annotate(
            max_rate=Max('savingoptions__intr_rate2')
        ).order_by('-max_rate')

    serializer = SavingProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saving_product_detail(request, product_pk):
    product = SavingProducts.objects.get(pk=product_pk)
    options = SavingOptions.objects.filter(product=product_pk)
    product_serializer = SavingProductsSerializer(product)
    option_serializer = SavingOptionsSerializer(options, many=True)

    serializer = {
        "product" : product_serializer.data,
       "options" : option_serializer.data
    }

    return Response(serializer, status=status.HTTP_200_OK)