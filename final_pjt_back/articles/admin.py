from django.contrib import admin
from .models import Article, Comment, Like, CommentLike

# User 모델 등록 제거
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(CommentLike)