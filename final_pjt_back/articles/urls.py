from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),                                # 게시글 목록 조회
    path('<int:article_pk>/', views.article_detail, name='article_detail'),           # 게시글 상세 조회 및 수정 및 삭제
    path('<int:article_pk>/comments/', views.comment_list, name='comment_list'),      # 댓글 목록 조회 및 생성
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'), # 댓글 상세 조회 및 수정 및 삭제
    path('<int:article_pk>/like/', views.article_like, name='article_like'),          # 게시글 좋아요 생성 및 삭제
    # path('<int:article_pk>/likes/', views.like_list),                               # 좋아요 목록 조회 및 생성
    # path('<int:article_pk>/likes/<int:like_pk>/', views.like_detail),               # 좋아요 상세 조회 및 수정 및 삭제
    # path('<int:article_pk>/comments/<int:comment_pk>/like/', views.comment_like),   # 댓글 좋아요 생성 및 삭제
   
]
