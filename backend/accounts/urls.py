from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FriendRequestViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'friend-requests', FriendRequestViewSet, basename='friendrequest')

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('check_auth/', views.check_auth, name='check_auth'),
    path('api/', include(router.urls)),
]