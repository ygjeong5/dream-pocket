from rest_framework import serializers
from .models import User, Ledger
from finlife.serializers import FinancialProductsSerializer
from finlife.models import FinancialProducts


class UserSerializer(serializers.ModelSerializer):
    products = FinancialProductsSerializer(many=True, read_only=True)
    # product_ids = serializers.ListField(
    #     child=serializers.IntegerField(), write_only=True, required=False
    # )

    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'gender', 'goal_amount', 'products', 'point')


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'user', 'date', 'category', 'amount', 'description']
        read_only_fields = ['user']
