from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialPost
from .serializers import FinancialPostSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def financial_post(request):
    if request.method == 'GET':
        posts = FinancialPost.objects.all().order_by('-created_at')
        serializer = FinancialPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.methos == 'POST':
        serializer = FinancialPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)