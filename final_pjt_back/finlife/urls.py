from django.urls import path
from . import views

app_name = 'finlife'

urlpatterns = [
    path('save-financial-products/', views.save_financial_products, name='sava_financial_products'),    # 금융 상품 데이터 저장
]
