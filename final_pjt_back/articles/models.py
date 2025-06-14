from django.db import models
from django.conf import settings


# 게시글 모델
class Article(models.Model):
    CATEGORY_CHOICES = [
        ('free', '자유게시판'),
        ('knowledge', '금융지식 나누기'),
        ('recommendation', '상품 추천'),
        ('notice', '공지사항'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='free'
    )


# 댓글 모델
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')


# 댓글 좋아요 모델
class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user} on comment {self.comment.id}"

# 조회수 모델
class View(models.Model):
    VIEW_TYPE_CHOICES = [
        ('article', 'Article'),
        ('comment', 'Comment'),
        ('like', 'Like'),
        ('comment_like', 'Comment Like'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20, choices=VIEW_TYPE_CHOICES)
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"View by {self.user} on {self.content_type} {self.object_id}"

# 조회수 모델
class ViewCount(models.Model):
    content_type = models.CharField(max_length=20, choices=View.VIEW_TYPE_CHOICES)
    object_id = models.PositiveIntegerField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.count} views on {self.content_type} {self.object_id}"
