from rest_framework import serializers
from .models import FinancialProducts, FinancialOptions, SavingProducts, SavingOptions

class FinancialOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOptions
        fields = '__all__'
         # read_only_fields = ('porduct',)


class FinancialProductsSerializer(serializers.ModelSerializer):
    options = FinancialOptionsSerializer(source='financialoptions', many=True)
    class Meta:
        model = FinancialProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    options = SavingOptionsSerializer(source='savingoptions', many=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'