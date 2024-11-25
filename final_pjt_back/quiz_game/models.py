from django.db import models

class Quiz(models.Model):
    LEVEL_CHOICES = [
        ('beginner', '초급'),
        ('intermediate', '중급'),
        ('advanced', '고급'),
    ]
    
    title = models.CharField(max_length=200)
    body = models.TextField()
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)
    choice_c = models.CharField(max_length=200)
    choice_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')