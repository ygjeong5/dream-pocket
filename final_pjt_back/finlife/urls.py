from django.urls import path
from . import views

app_name = 'finlife'

urlpatterns = [
    path('save-financial-products/', views.save_financial_products, name='sava_financial_products'),    # 금융 상품 데이터 저장
    path('rate/', views.exchange_rate, name='rate'),
    path('financial-products-list/', views.financial_products_list, name='financial_products_list'),
    path('financial-product/detail/<int:product_pk>/', views.financial_product_detail, name='financial_product_detail'),
]
