from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('users/', views.CustomUserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='user-detail'),
    path('login/', views.CustomUserLogin.as_view(), name='user-login'),
]
