from rest_framework import serializers
from .models import FinancialPost

class FinancialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialPost
        fields = ['id', 'title', 'content', 'keywords', 'created_at']