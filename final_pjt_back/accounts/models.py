from django.db import models
from django.contrib.auth.models import AbstractUser
from finlife.models import FinancialProducts


# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = [
        (0, 'Unknown'),
        (1, 'Male'),
        (2, 'Female'),
    ]
    age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    goal_amount = models.IntegerField(blank=True, null=True)
    products = models.ManyToManyField(FinancialProducts, blank=True)