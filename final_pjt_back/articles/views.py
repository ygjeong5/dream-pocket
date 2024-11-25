from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Article, Comment, Like
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# 게시글 목록 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-created_at')
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': '로그인이 필요합니다.'}, 
                          status=status.HTTP_401_UNAUTHORIZED)
            
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시글 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)
    
    if not request.user.is_authenticated:
        return Response({'error': '로그인이 필요합니다.'}, 
                      status=status.HTTP_401_UNAUTHORIZED)
        
    if request.user != article.user:
        return Response({'error': '권한이 없습니다.'}, 
                      status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 댓글 목록 조회 및 생성
@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    if not request.user.is_authenticated:
        return Response({'error': '로그인이 필요합니다.'}, 
                      status=status.HTTP_401_UNAUTHORIZED)
        
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 댓글 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return Response({'error': '권한이 없습니다.'}, 
                      status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 게시글 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    like_exists = article.like_set.filter(user=request.user).exists()
    
    if like_exists:
        article.like_set.filter(user=request.user).delete()
        is_liked = False
    else:
        Like.objects.create(user=request.user, article=article)
        is_liked = True
    
    return Response({
        'is_liked': is_liked,
        'like_count': article.like_set.count()
    })

