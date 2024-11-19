from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
import requests
from finlife.models import FinancialProducts

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    user = request.user
    product_ids = request.data.get('product_ids', []) # product_ids vue에서 res에 담아주는 값

    if not product_ids:
        return Response({"error": "No products selected"}, status=status.HTTP_400_BAD_REQUEST)

    # FinancialProducts에서 product_ids에 해당하는 상품들을 조회
    products = FinancialProducts.objects.filter(fin_prdt_cd__in=product_ids)

    # 유효한 상품 ID인지 확인
    if not products.exists():
        return Response({"error": "No valid products found"}, status=status.HTTP_404_NOT_FOUND)

    # 중복 추가 방지 및 추가 작업
    existing_products = user.products.filter(fin_prdt_cd__in=product_ids)
    new_products = products.exclude(fin_prdt_cd__in=existing_products.values_list('fin_prdt_cd', flat=True))

    # 새로운 상품이 있으면 추가
    if new_products.exists():
        user.products.add(*new_products)

        # 새로 추가된 상품들의 정보 반환
        added_products = [
            {"id": product.id, "name": product.fin_prdt_nm} for product in new_products
        ]
        return Response(
            {
                "message": "Products added successfully",
                "added_products": added_products,
            },
            status=status.HTTP_200_OK
        )

    # 이미 추가된 상품만 있을 경우
    existing_products_data = [
        {"id": product.id, "name": product.fin_prdt_nm} for product in existing_products
    ]
    return Response(
        {
            "message": "No new products added",
            "existing_products": existing_products_data,
        },
        status=status.HTTP_200_OK
    )