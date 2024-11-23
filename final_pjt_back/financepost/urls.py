from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.financial_post, name='financial_post'),
    path('financial-posts/<int:pk>/', views.financial_post_detail, name='financial_post_detail'), 
]
