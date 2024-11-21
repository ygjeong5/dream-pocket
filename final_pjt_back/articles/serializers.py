from rest_framework import serializers
from .models import Article, Comment, Like, View, ViewCount 
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """사용자 정보 시리얼라이저"""
    class Meta:
        model = User
        fields = ('id', 'username', 'age')

class CommentSerializer(serializers.ModelSerializer):
    """댓글 생성/수정 시리얼라이저"""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article', 'created_at')
        read_only_fields = ('user', 'article', 'likes')

class ArticleSerializer(serializers.ModelSerializer):
    """게시글 생성/수정 시리얼라이저"""
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user', 'comments', 'created_at', 'like_count', 'is_liked')
        read_only_fields = ('user', 'comments')

    def get_like_count(self, obj):
        return obj.like_set.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_set.filter(user=request.user).exists()
        return False

class LikeSerializer(serializers.ModelSerializer):
    """좋아요 시리얼라이저"""
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('user', 'article', 'likes')

class ArticleDetailSerializer(serializers.ModelSerializer):
    """게시글 상세 시리얼라이저"""
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    like_set = LikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'likes')
