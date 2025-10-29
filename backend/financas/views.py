from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q  # Correção aqui

from .models import Transaction, SharedPayment
from .serializers import (
    TransactionSerializer,
    CreateUpdateTransactionSerializer,
    SharedPaymentSerializer,
    ProcessPaymentSerializer
)
from .services import TransactionService

class TransactionListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUpdateTransactionSerializer
        return TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(
            Q(user=self.request.user) |
            Q(shares__shared_with=self.request.user)
        ).distinct()

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CreateUpdateTransactionSerializer
        return TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(
            Q(user=self.request.user) |
            Q(shares__shared_with=self.request.user)
        ).distinct()

class TransactionPaymentPlanView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            payment_plan = TransactionService.get_transaction_payment_plan(pk)
            return Response(payment_plan)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserFinancialSummaryView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            summary = TransactionService.get_user_financial_summary(request.user)
            return Response(summary)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class SharedPaymentListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SharedPaymentSerializer
    
    def get_queryset(self):
        return SharedPayment.objects.filter(
            transaction_share__shared_with=self.request.user
        ).order_by('due_date')

class PaymentToReceiveListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SharedPaymentSerializer
    
    def get_queryset(self):
        return SharedPayment.objects.filter(
            transaction_share__transaction__user=self.request.user,
            status='Pendente'
        ).order_by('due_date')

class ProcessPaymentView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProcessPaymentSerializer
    
    def post(self, request, payment_id):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            payment = TransactionService.process_payment(
                payment_id=payment_id,
                paid_by_user=request.user,
                payment_date=serializer.validated_data.get('payment_date'),
                amount=serializer.validated_data.get('amount')
            )
            
            return Response(
                SharedPaymentSerializer(payment).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CancelPaymentView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, payment_id):
        try:
            payment = TransactionService.cancel_payment(payment_id)
            return Response(
                SharedPaymentSerializer(payment).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class TransactionChoicesView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        choices = {
            "bancos": dict(Transaction.BANCO_CHOICES),
            "categorias": dict(Transaction.CATEGORIA_CHOICES),
            "tipos": dict(Transaction.TIPO_CHOICES),
            "formas": dict(Transaction.FORMA_CHOICES),
            "status_pagamento": dict(Transaction.STATUS_PAGAMENTO_CHOICES),
        }
        return Response(choices)



from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import SharedPayment
from .serializers import SharedPaymentSerializer, ProcessPaymentSerializer, SharedPaymentReadSerializer
# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Q, Sum
from .models import Transaction, SharedPayment
from .serializers import TransactionSerializer, SharedPaymentReadSerializer

# views.py
class MyDebtsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        print(f"🔍 MyDebtsListView - Filtros recebidos: {self.request.query_params}")
        
        # 🔥 CORREÇÃO: Filtrar apenas transações de SAÍDA (débitos)
        queryset = Transaction.objects.filter(
            user=self.request.user,
            tipo='Saída'  # Apenas saídas são consideradas dívidas
        ).order_by('-data', '-created_at')
        
        queryset = self.apply_filters(queryset)
        print(f"📊 MyDebtsListView - Resultados (apenas saídas): {queryset.count()} itens")
        return queryset
    
    
    def apply_filters(self, queryset):
        # Filtro por data
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                queryset = queryset.filter(data__gte=start_date)
            except ValueError:
                pass
        
        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                queryset = queryset.filter(data__lte=end_date)
            except ValueError:
                pass
        
        # Filtro por status
        status_param = self.request.query_params.get('status')
        if status_param:
            status_list = [s.strip() for s in status_param.split(',')]
            queryset = queryset.filter(status_pagamento__in=status_list)
        
        # Filtro por categoria
        categoria_param = self.request.query_params.get('categoria')
        if categoria_param:
            categoria_list = [c.strip() for c in categoria_param.split(',')]
            queryset = queryset.filter(categoria__in=categoria_list)
        
        return queryset


class MyReceivablesListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SharedPaymentReadSerializer
    
    def get_queryset(self):
        print(f"🔍 MyReceivablesListView - Filtros recebidos: {self.request.query_params}")
        queryset = SharedPayment.objects.select_related(
            'transaction_share__transaction', 
            'transaction_share__shared_with', 
            'received_by', 
            'paid_by'
        ).filter(
            transaction_share__transaction__user=self.request.user
        ).order_by('due_date')
        
        queryset = self.apply_filters(queryset)
        print(f"📊 MyReceivablesListView - Resultados: {queryset.count()} itens")
        return queryset
    
    def apply_filters(self, queryset):
        # Filtro por data
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                queryset = queryset.filter(due_date__gte=start_date)
            except ValueError:
                pass
        
        if end_date:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                queryset = queryset.filter(due_date__lte=end_date)
            except ValueError:
                pass
        
        # Filtro por status
        status_param = self.request.query_params.get('status')
        if status_param:
            status_list = [s.strip() for s in status_param.split(',')]
            queryset = queryset.filter(status__in=status_list)
        
        # Filtro por categoria (via transaction)
        categoria_param = self.request.query_params.get('categoria')
        if categoria_param:
            categoria_list = [c.strip() for c in categoria_param.split(',')]
            queryset = queryset.filter(
                transaction_share__transaction__categoria__in=categoria_list
            )
        
        return queryset

from django.db.models import Sum
from django.db.models.functions import TruncMonth

class MonthlyExpenseEvolutionView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Obter parâmetros de filtro
        months = int(request.query_params.get('months', 6))
        categoria = request.query_params.get('categoria')
        
        # Calcular data de início
        end_date = timezone.now().date()
        start_date = end_date - relativedelta(months=months-1)
        start_date = start_date.replace(day=1)  # Primeiro dia do mês
        
        # Query para agrupar gastos por mês
        expenses_by_month = Transaction.objects.filter(
            user=request.user,
            tipo='Saída',
            data__gte=start_date,
            data__lte=end_date
        )
        
        if categoria:
            expenses_by_month = expenses_by_month.filter(categoria=categoria)
        
        # Usar TruncMonth corretamente
        expenses_by_month = expenses_by_month.annotate(
            month=TruncMonth('data')  # Correto: usar TruncMonth diretamente
        ).values('month').annotate(
            total=Sum('valor')
        ).order_by('month')
        
        # Formatar dados para o gráfico
        chart_data = []
        current_date = start_date
        
        while current_date <= end_date:
            month_str = current_date.strftime('%Y-%m')
            total = 0
            
            # Encontrar o total para este mês
            for item in expenses_by_month:
                if item['month'].strftime('%Y-%m') == month_str:
                    total = float(item['total'] or 0)
                    break
            
            chart_data.append({
                'month': current_date.strftime('%b/%Y'),  # Formato: Jan/2024
                'total': total
            })
            
            # Próximo mês
            current_date = (current_date + relativedelta(months=1)).replace(day=1)
        
        return Response({
            'chart_data': chart_data,
            'period': f"{start_date.strftime('%b/%Y')} - {end_date.strftime('%b/%Y')}"
        })

class PayDebtView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, payment_id):
        try:
            # 1️⃣ Tenta buscar pagamento compartilhado
            payment = SharedPayment.objects.filter(id=payment_id).first()
            if payment:
                is_owner = payment.transaction_share.transaction.user == request.user
                is_shared_with_user = payment.transaction_share.shared_with == request.user
                if not (is_owner or is_shared_with_user):
                    return Response({"error": "Pagamento não encontrado ou não pertence a você"}, status=404)

                payment.mark_as_paid(
                    paid_by_user=request.user,
                    payment_date=timezone.now().date()
                )
                return Response(SharedPaymentReadSerializer(payment).data, status=200)

            # 2️⃣ Tenta buscar dívida própria
            try:
                transaction = Transaction.objects.get(id=payment_id, user=request.user)
                transaction.mark_as_paid(payment_date=timezone.now().date())
                return Response({"success": "Dívida paga com sucesso"}, status=200)
            except Transaction.DoesNotExist:
                return Response({"error": "Pagamento não encontrado ou não pertence a você"}, status=404)
                
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Case, When, Value, DecimalField, Q
from django.db.models.functions import TruncMonth, TruncYear
from django.utils import timezone
from datetime import timedelta
import calendar
from .models import Transaction

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Case, When, Value, DecimalField, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import timedelta
import calendar
import logging
from .models import Transaction

# Configurar logger
logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_financeiro(request):
    user = request.user
    period = request.GET.get('period', 'this_month')
    
    try:
        # Query base filtrada por usuário
        transactions = Transaction.objects.filter(user=user)
        
        # Aplicar filtro de período - CORREÇÃO: usar campo 'data' em vez de 'created_at'
        today = timezone.now().date()
        
        if period == 'this_month':
            first_day = today.replace(day=1)
            last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])
            transactions = transactions.filter(data__range=[first_day, last_day])
        
        elif period == 'last_month':
            first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
            last_day_last_month = first_day_last_month.replace(
                day=calendar.monthrange(first_day_last_month.year, first_day_last_month.month)[1]
            )
            transactions = transactions.filter(data__range=[first_day_last_month, last_day_last_month])
        
        elif period == 'last_3_months':
            three_months_ago = today - timedelta(days=90)
            transactions = transactions.filter(data__gte=three_months_ago)
        
        elif period == 'last_6_months':
            six_months_ago = today - timedelta(days=180)
            transactions = transactions.filter(data__gte=six_months_ago)
        
        elif period == 'last_year':
            first_day_last_year = today.replace(year=today.year-1, month=1, day=1)
            last_day_last_year = today.replace(year=today.year-1, month=12, day=31)
            transactions = transactions.filter(data__range=[first_day_last_year, last_day_last_year])
        
        elif period == 'this_year':
            first_day_this_year = today.replace(month=1, day=1)
            transactions = transactions.filter(data__gte=first_day_this_year)
        
        # Resto do código permanece igual...
        dashboard_agg = transactions.aggregate(
            entrada=Sum(
                Case(
                    When(tipo='Entrada', then='valor'),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            ),
            saida_credito=Sum(
                Case(
                    When(status_pagamento='Pendente', then='valor'),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            ),
            saida_debito=Sum(
                Case(
                    When(tipo='Saída', then='valor'),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            )
        )
        
        entrada = dashboard_agg['entrada'] or 0
        saida_credito = dashboard_agg['saida_credito'] or 0
        saida_debito = dashboard_agg['saida_debito'] or 0
        saida_total = saida_credito + saida_debito
        saldo_total = entrada - saida_total
        
        dashboard_data = {
            'entrada': float(entrada),
            'saida': float(saida_total),
            'saldo_total': float(saldo_total)
        }
        
        # 2. Dados por categoria (gastos)
        categorias_data = transactions.filter(
            tipo='Saída'
        ).values('categoria').annotate(
            gasto=Sum(
                Case(
                               When(
                Q(forma='Crédito', status_pagamento='Pendente') |
                Q(forma='Débito') |
                Q(forma='Pix') |
                Q(forma='Dinheiro') |
                Q(forma='Transferência'),
                then='valor'
            ),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            )
        ).order_by('-gasto')
        
        # Converter para lista de dicionários
        categorias_gasto = []
        for cat in categorias_data:
            categorias_gasto.append({
                'categoria': cat['categoria'],
                'gasto': float(cat['gasto'] or 0)
            })
        
        # 3. Percentual por categoria - CORREÇÃO: usar total de gastos em vez de saldo_total
        total_gastos = sum(cat['gasto'] for cat in categorias_gasto)
        categorias_percentual = []
        
        for cat in categorias_gasto:
            gasto = cat['gasto']
            if total_gastos > 0:
                percentual = (gasto / total_gastos) * 100
            else:
                percentual = 0
                
            categorias_percentual.append({
                'categoria': cat['categoria'],
                'total_pago': gasto,
                'percentual': round(percentual, 2)
            })
        
        # 4. Dados mensais para gráfico - CORREÇÃO: usar campo 'data' em vez de 'created_at'
        meses_data = transactions.annotate(
            mes_ano=TruncMonth('data')
        ).values('mes_ano').annotate(
            entrada=Sum(
                Case(
                    When(
                        Q(tipo='Entrada'),
                        then='valor'
                    ),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            ),
            saida=Sum(
                Case(
                    When(
                        Q(tipo='Saída'),
                        then='valor'
                    ),
                    default=Value(0),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )
            )
        ).order_by('mes_ano')

        meses_formatados = []
        for item in meses_data:
            if item['mes_ano']:
                meses_formatados.append({
                    'mes_ano': item['mes_ano'].strftime('%m/%Y'),
                    'entrada': float(item['entrada'] or 0),
                    'saida': float(item['saida'] or 0)
                })
        
        return Response({
            'dashboard': dashboard_data,
            'categorias_gasto': categorias_gasto,
            'categorias_percentual': categorias_percentual,
            'grafico_mensal': meses_formatados
        })
    
    except Exception as e:
        logger.error(f"Erro no dashboard: {str(e)}", exc_info=True)
        return Response(
            {'error': 'Erro interno do servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )