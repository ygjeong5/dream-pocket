from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Article, Comment, Like, CommentLike
from .serializers import (ArticleSerializer, CommentSerializer, LikeSerializer, ArticleDetailSerializer)
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .serializers import UserSerializer


# 게시글 목록 조회 및 생성
@api_view(['GET', 'POST'])
def article_list(request):
    # 게시글 목록 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data) 
    
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 상세 조회 및 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
        
        # 상세 조회 (GET)
        if request.method == 'GET':
            serializer = ArticleSerializer(article, context={'request': request})
            return Response(serializer.data)
        
        # 수정 (PUT)
        elif request.method == 'PUT':
            if request.user != article.user:
                return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
        # 삭제 (DELETE)
        elif request.method == 'DELETE':
            if request.user != article.user:
                return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Article.DoesNotExist:
        return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

# 댓글 목록 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
        
        if request.method == 'GET':
            comments = article.comments.all()  # related_name 사용
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            print("요청 데이터:", request.data)
            serializer = CommentSerializer(data={
                'content': request.data.get('content'),
                'article': article.pk
            })
            
            if serializer.is_valid():
                serializer.save(user=request.user, article=article)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("유효성 검사 오류:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Article.DoesNotExist:
        return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 댓글 수정 및 삭제를 위한 새로운 뷰 함수 추가
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk, article_id=article_pk)
        
        if request.method == 'PUT':
            if request.user != comment.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
                
        elif request.method == 'DELETE':
            if request.user != comment.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 게시글 좋아요 생성 및 삭제
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
        if article.like_set.filter(user=request.user).exists():
            article.like_set.filter(user=request.user).delete()
            is_liked = False
        else:
            Like.objects.create(user=request.user, article=article)
            is_liked = True
        
        return Response({
            'is_liked': is_liked,
            'like_count': article.like_set.count()
        })
    except Article.DoesNotExist:
        return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

# # 좋아요 목록 조회 및 생성
# @api_view(['GET', 'POST'])
# def like_list(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     # 좋아요 목록 조회
#     if request.method == 'GET':
#         likes = article.like_set.all()
#         serializer = LikeSerializer(likes, many=True)
#         return Response(serializer.data)

# # 좋아요 상세 조회 및 수정 및 삭제
# @api_view(['GET', 'PUT', 'DELETE'])
# def like_detail(request, article_pk, like_pk):
#     like = get_object_or_404(Like, pk=like_pk)
#     # 좋아요 상세 조회
#     if request.method == 'GET':
#         serializer = LikeSerializer(like)
#         return Response(serializer.data)


# # 댓글 좋아요 생성 및 삭제
# @api_view(['POST', 'DELETE'])
# def comment_like(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     # 댓글 좋아요 생성
#     if request.method == 'POST':
#         serializer = LikeSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(comment=comment, user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# # 게시글 조회수 증가
# @api_view(['POST'])
# def article_view(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     article.view_count += 1
#     article.save()
#     return Response(status=status.HTTP_200_OK)

# # 댓글 조회수 증가
# @api_view(['POST'])
# def comment_view(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     comment.view_count += 1
#     comment.save()
#     return Response(status=status.HTTP_200_OK)

# # 좋아요 조회수 증가
# @api_view(['POST'])
# def like_view(request, like_pk):
#     like = get_object_or_404(Like, pk=like_pk)
#     like.view_count += 1
#     like.save()
#     return Response(status=status.HTTP_200_OK)

# # 댓글 좋아요 조회수 증가
# @api_view(['POST'])
# def comment_like_view(request, comment_like_pk):
#     comment_like = get_object_or_404(CommentLike, pk=comment_like_pk)
#     comment_like.view_count += 1
#     comment_like.save()
#     return Response(status=status.HTTP_200_OK)

# # 게시글 조회수 증가
# @api_view(['POST'])
# def article_view_count(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     article.view_count += 1
#     article.save()
#     return Response(status=status.HTTP_200_OK)

# # 댓글 조회수 증가
# @api_view(['POST'])
# def comment_view_count(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     comment.view_count += 1
#     comment.save()
#     return Response(status=status.HTTP_200_OK)

# # 게시글 목록 조회 및 생성
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # JWT 인증 설정
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     # 게시글 생성
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     # 권한 설정
#     def get_permissions(self):
#         # GET 요청은 인증 없이 허용
#         if self.action in ['list', 'retrieve']:
#             permission_classes = []
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]

# # 유저 정보 조회
# @api_view(['GET'])
# def user_detail(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)

