from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
import requests
from .serializers import UserSerializer

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(
            user, data = request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)