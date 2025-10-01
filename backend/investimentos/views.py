# investimentos/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Sum, Q
from decimal import Decimal
from .models import Investimento, Rendimento
from .serializers import InvestimentoSerializer, RendimentoSerializer
from rest_framework.views import APIView

class InvestimentoListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        return InvestimentoSerializer
    
    def get_queryset(self):
        # Filtra apenas investimentos do usuário autenticado
        # Igual ao padrão do TransactionListView
        return Investimento.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # O user será automaticamente adicionado pelo HiddenField no serializer
        serializer.save()
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Aplicar filtros como no TransactionListView
            tipo_filtro = request.GET.get('tipo')
            if tipo_filtro:
                queryset = queryset.filter(tipo=tipo_filtro)
            
            search_term = request.GET.get('search')
            if search_term:
                queryset = queryset.filter(
                    Q(nome_patrimonio__icontains=search_term) |
                    Q(instituicao__icontains=search_term)
                )
            
            # Ordenação
            queryset = queryset.order_by('-data_compra')
            
            serializer = self.get_serializer(queryset, many=True)
            
            # Calcular totais (opcional)
            portfolio_total = queryset.aggregate(
                total=Sum('valor_total')
            )['total'] or Decimal('0.00')
            
            response_data = {
                'investimentos': serializer.data,
                'portfolio_total': portfolio_total,
                'count': queryset.count()
            }
            
            return Response(response_data)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao carregar investimentos: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

class InvestimentoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InvestimentoSerializer
    
    def get_queryset(self):
        # Filtra apenas investimentos do usuário autenticado
        return Investimento.objects.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data = {
                'message': 'Investimento atualizado com sucesso!',
                'data': response.data
            }
            return response
        except Exception as e:
            return Response(
                {'error': f'Erro ao atualizar investimento: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response(
                {'message': 'Investimento excluído com sucesso!'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': f'Erro ao excluir investimento: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

class RendimentoListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RendimentoSerializer
    
    def get_queryset(self):
        # Filtra rendimentos de investimentos do usuário autenticado
        return Rendimento.objects.filter(investimento__user=self.request.user)
    
    def perform_create(self, serializer):
        # Verificar se o investimento pertence ao usuário
        investimento_id = self.request.data.get('investimento')
        try:
            investimento = Investimento.objects.get(id=investimento_id, user=self.request.user)
            serializer.save()
        except Investimento.DoesNotExist:
            raise serializers.ValidationError({
                'investimento': 'Investimento não encontrado ou não pertence ao usuário.'
            })
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            self.perform_create(serializer)
            
            return Response(
                {
                    'message': 'Rendimento registrado com sucesso!',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao registrar rendimento: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

class RendimentoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RendimentoSerializer
    
    def get_queryset(self):
        # Filtra rendimentos de investimentos do usuário autenticado
        return Rendimento.objects.filter(investimento__user=self.request.user)

class InvestimentoDashboardAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            # Filtra apenas investimentos do usuário autenticado
            investimentos = Investimento.objects.filter(user=request.user)
            
            # Calcular totais
            portfolio_total = investimentos.aggregate(
                total=Sum('valor_total')
            )['total'] or Decimal('0.00')
            
            # Últimos investimentos
            ultimos_investimentos = investimentos.order_by('-data_compra')[:5]
            serializer = InvestimentoSerializer(ultimos_investimentos, many=True)
            
            # Rendimentos recentes
            rendimentos_recentes = Rendimento.objects.filter(
                investimento__user=request.user
            ).order_by('-data')[:10]
            rendimentos_serializer = RendimentoSerializer(rendimentos_recentes, many=True)
            
            return Response({
                'investimentos_recentes': serializer.data,
                'rendimentos_recentes': rendimentos_serializer.data,
                'portfolio_total': portfolio_total,
                'total_investimentos': investimentos.count()
            })
            
        except Exception as e:
            return Response(
                {'error': f'Erro no dashboard: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )