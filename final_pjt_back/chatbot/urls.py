from django.contrib import admin
from django.urls import path
from .views import chat_message

app_name = 'chatbot'
urlpatterns = [
    path('chat_message/', chat_message, name='chat_message'),

]