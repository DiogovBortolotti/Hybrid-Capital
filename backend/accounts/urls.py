from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'invitations', views.InvitationViewSet, basename='invitation')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('check_auth/', views.check_auth, name='check_auth'),
    path('api/', include(router.urls)),  # Changed from 'api/' to root
]