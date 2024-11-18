from django.urls import path, include
from . import views
from .views import UpdateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from dj_rest_auth.views import LoginView, LogoutView


app_name='accounts'
urlpatterns = [
    # path('login/', views.login, name='login'),
    path('user/update/', UpdateUserView.as_view(), name='update-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 액세스 토큰과 리프레시 토큰 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 리프레시 토큰을 이용한 액세스 토큰 갱신
    # 회원가입
    path('signup/', include('dj_rest_auth.registration.urls')),  # dj_rest_auth의 회원가입 URL 포함
    # 로그아웃 (JWT 토큰 제거)
    path('logout/', LogoutView.as_view(), name='logout'),  # 로그아웃 처리
]
