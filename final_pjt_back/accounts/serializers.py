from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model


# class CustomRegisterSerializer(RegisterSerializer):
#     # birth_date = serializers.DateField(required=False)
#     # address = serializers.CharField(max_length=255, required=False)

#     def custom_signup(self, request, user):
#         # user.birth_date = self.validated_data.get('birth_date', None)
#         # user.address = self.validated_data.get('address', None)
#         user.save()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'birth_date', 'address']  # 수정 가능한 필드들