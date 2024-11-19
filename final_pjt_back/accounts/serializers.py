from rest_framework import serializers
from .models import User
from finlife.serializers import FinancialProductsSerializer
from finlife.models import FinancialProducts


class UserSerializer(serializers.ModelSerializer):
    products = FinancialProductsSerializer(many=True, read_only=True)
    # product_ids = serializers.ListField(
    #     child=serializers.IntegerField(), write_only=True, required=False
    # )

    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'gender', 'goal_amount', 'products')