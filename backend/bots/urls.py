from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('adicionar_chave/', views.adicionar_chave, name='adicionar_chave'),
    path('iniciar/<int:chave_id>/', views.iniciar_monitoramento, name='iniciar_monitoramento'),
]
