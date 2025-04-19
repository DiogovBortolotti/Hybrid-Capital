# urls.py
from django.urls import path
from .views import TransactionCreateView, TransactionChoicesView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction-choices/', TransactionChoicesView.as_view(), name='transaction-choices'),
]