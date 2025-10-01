# investimentos/urls.py
from django.urls import path
from . import views

app_name = 'investimentos'

urlpatterns = [
    # Dashboard
    path('', views.InvestimentoDashboardAPIView.as_view(), name='dashboard'),
    
    # Investimentos (padrão REST)
    path('investimentos/', views.InvestimentoListCreateAPIView.as_view(), name='investimento-list'),
    path('investimentos/<int:pk>/', views.InvestimentoDetailAPIView.as_view(), name='investimento-detail'),
    
    # Rendimentos (padrão REST)
    path('rendimentos/', views.RendimentoListCreateAPIView.as_view(), name='rendimento-list'),
    path('rendimentos/<int:pk>/', views.RendimentoDetailAPIView.as_view(), name='rendimento-detail'),
    
    # URLs alternativas para compatibilidade (OPCIONAL)
    path('criar/', views.InvestimentoListCreateAPIView.as_view(), name='investimento-criar'),
    path('listar/', views.InvestimentoListCreateAPIView.as_view(), name='investimento-listar'),
]