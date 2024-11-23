from django.db import models

# Create your models here.
class FinancialPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    keywords = models.CharField(max_length=300, help_text="Comma-separated keywords")
    created_at = models.DateTimeField(auto_now_add=True)
