from django.urls import path
from . import views

app_name = "quiz_game"
urlpatterns = [
    path('quiz/random/<int:count>/', views.random_quiz, name='random_quiz'),
    path('quiz-info/', views.quiz_info, name='quoz_info'),
]