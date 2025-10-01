# investimentos/models.py
from django.db import models
from django.conf import settings

class Investimento(models.Model):
    TIPOS = (
        ('ACAO', 'Ação'),
        ('FII', 'Fundo Imobiliário (FII)'),
        ('CRIPTO', 'Criptomoeda'),
        ('TESOURO', 'Tesouro/Selic'),
        ('POUPANCA', 'Poupança'),
        ('CDB', 'CDB'),
        ('LCI', 'LCI'),
        ('LCA', 'LCA'),
    )
    
    MOEDAS = (
        ('BRL', 'Real'),
        ('USD', 'Dólar'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    tipo = models.CharField(max_length=10, choices=TIPOS, verbose_name='Tipo de Investimento')
    instituicao = models.CharField(max_length=100, verbose_name='Instituição')
    nome_patrimonio = models.CharField(max_length=100, verbose_name='Nome do Ativo')
    valor_cota = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor da Cota')
    unidades = models.DecimalField(max_digits=15, decimal_places=6, verbose_name='Quantidade')
    valor_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name='Valor Total')
    data_compra = models.DateField(verbose_name='Data da Compra')
    moeda = models.CharField(max_length=3, choices=MOEDAS, default='BRL', verbose_name='Moeda')
    cotacao_dolar_pago = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Cotação do Dólar')
    taxa_anual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Taxa Anual (%)')
    aporte_mensal = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='Aporte Mensal')
    prazo_meses = models.IntegerField(null=True, blank=True, verbose_name='Prazo (meses)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    def save(self, *args, **kwargs):
        # Calcular valor total automaticamente
        if self.valor_cota and self.unidades:
            self.valor_total = self.valor_cota * self.unidades
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nome_patrimonio} - {self.get_tipo_display()}"
    
    class Meta:
        verbose_name = 'Investimento'
        verbose_name_plural = 'Investimentos'
        ordering = ['-data_compra']


class Rendimento(models.Model):
    investimento = models.ForeignKey(
        Investimento,
        on_delete=models.CASCADE,
        related_name='rendimentos'
    )
    valor = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor do Rendimento')
    data = models.DateField(verbose_name='Data do Rendimento')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Rendimento {self.valor} - {self.investimento.nome_patrimonio}"
    
    class Meta:
        ordering = ['-data']