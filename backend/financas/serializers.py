# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Transaction, TransactionShare, SharedPayment
from .services import TransactionService

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'email', 'full_name']

class SharedPaymentSerializer(serializers.ModelSerializer):
    paid_by = UserSerializer(read_only=True)
    received_by = UserSerializer(read_only=True)
    
    class Meta:
        model = SharedPayment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class TransactionShareSerializer(serializers.ModelSerializer):
    shared_with = UserSerializer(read_only=True)
    shared_with_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='shared_with'
    )
    payments = SharedPaymentSerializer(many=True, read_only=True)
    
    class Meta:
        model = TransactionShare
        fields = [
            'id', 'shared_with', 'shared_with_id', 'percentage', 
            'installments', 'payments', 'created_at'
        ]
        extra_kwargs = {
            'percentage': {'min_value': 0, 'max_value': 100}
        }

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    shares = TransactionShareSerializer(many=True, required=False)
    
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

class CreateUpdateTransactionSerializer(serializers.ModelSerializer):
    shares = TransactionShareSerializer(many=True, required=False, write_only=True)
    
    class Meta:
        model = Transaction
        exclude = ['user']
    
    def create(self, validated_data):
        shares_data = validated_data.pop('shares', [])
        user = self.context['request'].user
        return TransactionService.create_complete_transaction(
            user,
            validated_data,
            shares_data
        )
    
    def update(self, instance, validated_data):
        shares_data = validated_data.pop('shares', None)
        if shares_data is not None:
            TransactionService.update_transaction_shares(instance, shares_data)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class ProcessPaymentSerializer(serializers.Serializer):
    payment_date = serializers.DateField(required=False)
    amount = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2,
        required=False
    )
    
    def validate(self, attrs):
        if 'amount' in attrs and attrs['amount'] <= 0:
            raise serializers.ValidationError("O valor deve ser positivo")
        return attrs
    


class TransactionReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'banco', 'categoria', 'tipo', 'forma', 'valor', 'descricao', 'data', 'status_pagamento', 'user']

class TransactionShareReadSerializer(serializers.ModelSerializer):
    transaction = TransactionReadSerializer(read_only=True)
    shared_with = UserSerializer(read_only=True)
    
    class Meta:
        model = TransactionShare
        fields = ['id', 'transaction', 'shared_with', 'percentage', 'installments']

class SharedPaymentReadSerializer(serializers.ModelSerializer):
    transaction_share = TransactionShareReadSerializer(read_only=True)
    received_by = UserSerializer(read_only=True)
    paid_by = UserSerializer(read_only=True)
    
    class Meta:
        model = SharedPayment
        fields = ['id', 'amount', 'due_date', 'installment_number', 'status', 'payment_date', 'transaction_share', 'received_by', 'paid_by', 'created_at', 'updated_at']




from rest_framework import serializers
from .models import Transaction

class DashboardSerializer(serializers.Serializer):
    entrada = serializers.DecimalField(max_digits=15, decimal_places=2)
    saida = serializers.DecimalField(max_digits=15, decimal_places=2)
    saldo_total = serializers.DecimalField(max_digits=15, decimal_places=2)

class CategoriaGastoSerializer(serializers.Serializer):
    categoria = serializers.CharField()
    gasto = serializers.DecimalField(max_digits=15, decimal_places=2)

class CategoriaPercentualSerializer(serializers.Serializer):
    categoria = serializers.CharField()
    total_pago = serializers.DecimalField(max_digits=15, decimal_places=2)
    percentual = serializers.DecimalField(max_digits=5, decimal_places=2)

class MesGraficoSerializer(serializers.Serializer):
    mes_ano = serializers.CharField()
    entrada = serializers.DecimalField(max_digits=15, decimal_places=2)
    saida = serializers.DecimalField(max_digits=15, decimal_places=2)