from django.forms import ValidationError
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
import logging
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FriendRequest, CustomUser
from .serializers import FriendRequestSerializer, UserSerializer, CustomUserSerializer
from django.db import IntegrityError



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
    

from django.db.models import Q

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        email = self.request.query_params.get('email', None)
        if email:
            queryset = queryset.filter(Q(email__icontains=email))  # Filtra por email
        return queryset

    @action(detail=False, methods=['get'], url_path='me/friends')
    def my_friends(self, request):
        user = request.user
        sent = FriendRequest.objects.filter(from_user=user, is_accepted=True).values_list('to_user', flat=True)
        received = FriendRequest.objects.filter(to_user=user, is_accepted=True).values_list('from_user', flat=True)
        friends_ids = list(sent) + list(received)
        friends = CustomUser.objects.filter(id__in=friends_ids)
        return Response(UserSerializer(friends, many=True).data)



class FriendRequestViewSet(viewsets.ModelViewSet):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, is_accepted=False)

    def perform_create(self, serializer):
        from_user = self.request.user
        to_user = serializer.validated_data['to_user']

        if from_user == to_user:
            raise ValidationError(
                {"detail": "Você não pode se adicionar como amigo."},
                code=status.HTTP_400_BAD_REQUEST
            )
        
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            raise ValidationError(
                {"detail": "Você já enviou um convite para este usuário ou já são amigos."},
                code=status.HTTP_400_BAD_REQUEST
            )
    
        serializer.save(from_user=from_user)

    def handle_exception(self, exc):
        if isinstance(exc, (ValidationError, IntegrityError)):
            return Response(
                {"detail": str(exc)},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().handle_exception(exc)

    @action(detail=True, methods=['post'], url_path='accept')
    def accept(self, request, pk=None):
        friend_request = self.get_object()
        if friend_request.to_user != request.user:
            return Response({'error': 'Você não tem permissão.'}, status=403)
        friend_request.accept()
        return Response({'status': 'convite aceito'})

    @action(detail=False, methods=['delete'], url_path='remove-friend/(?P<friend_id>[^/.]+)')
    def remove_friend(self, request, friend_id=None):
        try:
            friend = CustomUser.objects.get(id=friend_id)
            user = request.user
            
            FriendRequest.objects.filter(
                (Q(from_user=user, to_user=friend) | Q(from_user=friend, to_user=user)),
                is_accepted=True
            ).delete()
            
            return Response({'status': 'amizade removida'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='list-users')
    def list_users(self, request):
        search_query = request.query_params.get('search', '')
        email_query = request.query_params.get('email', '')
        
        queryset = CustomUser.objects.exclude(id=request.user.id)
        
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) |
                Q(username__icontains=search_query))
        elif email_query:
            queryset = queryset.filter(email__iexact=email_query)
        
        friend_ids = request.user.friends.values_list('id', flat=True)
        queryset = queryset.exclude(id__in=friend_ids)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)