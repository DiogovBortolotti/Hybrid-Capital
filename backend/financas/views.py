from rest_framework import generics
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views import View
from .models import Transaction

class TransactionCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TransactionChoicesView(View):
    def get(self, request, *args, **kwargs):
        choices = {
            "bancos": dict(Transaction.BANCO_CHOICES),
            "categorias": dict(Transaction.CATEGORIA_CHOICES),
            "tipos": dict(Transaction.TIPO_CHOICES),
            "formas": dict(Transaction.FORMA_CHOICES),
            "status_pagamento": dict(Transaction.STATUS_PAGAMENTO_CHOICES),
        }
        return JsonResponse(choices)