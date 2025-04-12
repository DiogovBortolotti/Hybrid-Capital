from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        logger.info("Dados recebidos no registro: %s", request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            logger.info("Dados válidos: %s", serializer.validated_data)
            password = serializer.validated_data.get('password')
            try:
                validate_password(password)
            except ValidationError as e:
                logger.error("Erro na validação da senha: %s", e.messages)
                return Response({"password": e.messages}, status=status.HTTP_400_BAD_REQUEST)

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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)

    return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
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
