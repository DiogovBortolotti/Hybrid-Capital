from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.db import models  # For models.Q
import logging

# Relative imports from current app
from .models import Invitation, CustomUser
from .serializers import (
    CustomUserSerializer, 
    InvitationSerializer,
    UserSerializer,
    SendInvitationSerializer,
    HandleInvitationSerializer
)

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        logger.info("Dados recebidos no registro: %s", request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            logger.info("Dados válidos: %s", serializer.validated_data)
            user = serializer.save()
            logger.info("Usuário criado com sucesso: %s", user)

            token, created = Token.objects.get_or_create(user=user)
            logger.info("Token gerado: %s", token.key)

            return Response({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name,
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        else:
            logger.error("Erros no serializer: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error("Erro inesperado no registro: %s", str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
            },
            "token": token.key
        }, status=status.HTTP_200_OK)

    return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    try:
        user = request.user
        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
            }
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class InvitationViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Invitation.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'send':
            return SendInvitationSerializer
        elif self.action in ['accept', 'reject']:
            return HandleInvitationSerializer
        return InvitationSerializer
    
    def list(self, request):
        queryset = self.queryset.filter(
            models.Q(sender=request.user) | 
            models.Q(recipient=request.user)
        ).select_related('sender', 'recipient')
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'received': serializer.data,
            'sent': serializer.data,
            'current_user': UserSerializer(request.user).data
        })
    
    @action(detail=False, methods=['post'])
    def send(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        invitation = Invitation.objects.create(
            sender=request.user,
            recipient=serializer.validated_data['recipient_email']
        )
        
        return Response(
            InvitationSerializer(invitation, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=False, methods=['post'])
    def accept(self, request):
        return self._handle_invitation(request, 'accept')
    
    @action(detail=False, methods=['post'])
    def reject(self, request):
        return self._handle_invitation(request, 'reject')
    
    def _handle_invitation(self, request, action):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        invitation = serializer.validated_data['invitation_id']
        if action == 'accept':
            invitation.accept(request.user)
        else:
            invitation.reject()
        
        return Response(
            InvitationSerializer(invitation, context=self.get_serializer_context()).data
        )

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        # Exclui o usuário atual e usuários que já receberam convite
        sent_to_users = Invitation.objects.filter(
            sender=self.request.user
        ).values_list('recipient', flat=True)
        
        return CustomUser.objects.exclude(
            id=self.request.user.id
        ).exclude(
            id__in=sent_to_users
        ).order_by('email')