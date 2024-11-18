from rest_framework import serializers
from .models import FinancialProducts, FinancialOptions

class FinancialProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProducts
        fields = '__all__'


class FinancialOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOptions
        fields = '__all__'
        # read_only_fields = ('porduct',)