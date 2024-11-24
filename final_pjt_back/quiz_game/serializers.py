from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'body', 'choice_a', 'choice_b', 'choice_c', 'choice_d', 'correct_answer')