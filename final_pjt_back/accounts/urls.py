from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('user-info/', views.user_info),
    path('ledgers/', views.ledger_list_create, name='ledger-list-create'),  # List & Create
    path('ledgers/<int:pk>/', views.ledger_detail, name='ledger-detail'),   # Retrieve, Update, Delete
]
