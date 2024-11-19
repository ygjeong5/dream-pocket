from rest_framework import serializers
from .models import Article, Comment, Like, View, ViewCount 
from accounts.models import User

# 유저 정보 조회
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'age', ...)

# 게시글 생성 및 조회
class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

# 댓글 생성 및 조회
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article')

# 좋아요 생성 및 조회
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('user', 'article')

# 게시글 목록 조회
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')

# 댓글 목록 조회
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at')

# 좋아요 목록 조회
class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'created_at', 'updated_at')

# 게시글 상세 조회
class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)
    like_set = LikeListSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

# 조회수 목록 조회  
class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
        read_only_fields = ('user',)    
