from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.financial_post, name='financial_post')
]
