from django.urls import path
from . import views

app_name = 'chatbot'
urlpatterns = [
    path('chat_message/', views.chat_message, name='chat_message'),
    path('recommend/', views.recommend, name='recommend'),
]