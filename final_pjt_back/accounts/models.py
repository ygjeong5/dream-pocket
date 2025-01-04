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
    point = models.IntegerField(default=0)


class Ledger(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ledgers')
    date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
