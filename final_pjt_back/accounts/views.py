from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Ledger
from .serializers import UserSerializer, LedgerSerializer
from django.http import JsonResponse
import requests

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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ledger_list_create(request):
    # GET: 사용자 Ledger 목록 조회
    if request.method == 'GET':
        ledgers = Ledger.objects.filter(user=request.user)
        serializer = LedgerSerializer(ledgers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Ledger 생성
    elif request.method == 'POST':
        serializer = LedgerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ledger_detail(request, pk):
    try:
        ledger = Ledger.objects.get(pk=pk, user=request.user)
    except Ledger.DoesNotExist:
        return Response({'error': 'Ledger not found'}, status=status.HTTP_404_NOT_FOUND)

    # GET: Ledger 상세 조회
    if request.method == 'GET':
        serializer = LedgerSerializer(ledger)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Ledger 업데이트
    elif request.method == 'PUT':
        serializer = LedgerSerializer(ledger, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    # DELETE: Ledger 삭제
    elif request.method == 'DELETE':
        ledger.delete()
        return Response({'message': 'Ledger deleted successfully'}, status=status.HTTP_204_NO_CONTENT)