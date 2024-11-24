from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import LedgerViewSet

router = DefaultRouter()
router.register(r'ledgers', LedgerViewSet, basename='ledger')

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('user-info/', views.user_info),
    path('ledgers/', include(router.urls)),  # Router에 정의된 URL 포함
]
