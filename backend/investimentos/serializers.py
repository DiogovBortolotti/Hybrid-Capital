# investimentos/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Investimento, Rendimento

User = get_user_model()

class InvestimentoSerializer(serializers.ModelSerializer):
    # O campo user será automaticamente preenchido com o usuário autenticado
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Investimento
        fields = [
            'id', 'user', 'tipo', 'instituicao', 'nome_patrimonio', 
            'valor_cota', 'unidades', 'valor_total', 'data_compra',
            'moeda', 'cotacao_dolar_pago', 'taxa_anual', 'aporte_mensal',
            'prazo_meses', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'valor_total', 'created_at', 'updated_at']
    
    def validate_valor_cota(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor da cota deve ser maior que zero.")
        return value
    
    def validate_unidades(self, value):
        if value <= 0:
            raise serializers.ValidationError("A quantidade deve ser maior que zero.")
        return value


class RendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rendimento
        fields = ['id', 'investimento', 'valor', 'data', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate(self, data):
        # Verificar se o investimento pertence ao usuário autenticado
        investimento = data.get('investimento')
        if investimento and investimento.user != self.context['request'].user:
            raise serializers.ValidationError({
                'investimento': 'Este investimento não pertence ao usuário.'
            })
        return data