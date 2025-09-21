# urls.py
from django.urls import path
from .views import (
    TransactionListView,
    TransactionDetailView,
    TransactionPaymentPlanView,
    UserFinancialSummaryView,
    SharedPaymentListView,
    PaymentToReceiveListView,
    ProcessPaymentView,
    CancelPaymentView,
    TransactionChoicesView, dashboard_financeiro  
)
from .views import MyDebtsListView, MyReceivablesListView, PayDebtView, MonthlyExpenseEvolutionView


urlpatterns = [
    # Transações
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/payment-plan/', TransactionPaymentPlanView.as_view(), name='transaction-payment-plan'),
    
    # Choices
    path('transaction-choices/', TransactionChoicesView.as_view(), name='transaction-choices'),
    
    # Resumo financeiro
    path('financial-summary/', UserFinancialSummaryView.as_view(), name='financial-summary'),
    
    # Pagamentos
    path('shared-payments/', SharedPaymentListView.as_view(), name='shared-payment-list'),
    path('payments-to-receive/', PaymentToReceiveListView.as_view(), name='payment-to-receive-list'),
    path('payments/<int:payment_id>/process/', ProcessPaymentView.as_view(), name='process-payment'),
    path('payments/<int:payment_id>/cancel/', CancelPaymentView.as_view(), name='cancel-payment'),


    path("minhas-dividas/", MyDebtsListView.as_view(), name="minhas-dividas"),
    path("meus-recebimentos/", MyReceivablesListView.as_view(), name="meus-recebimentos"),
    path("pagar-divida/<int:payment_id>/", PayDebtView.as_view(), name="pagar-divida"),
    path('evolucao-mensal/', MonthlyExpenseEvolutionView.as_view(), name='evolucao-mensal'),


    path('dashboard/', dashboard_financeiro, name='dashboard-financeiro'),
]