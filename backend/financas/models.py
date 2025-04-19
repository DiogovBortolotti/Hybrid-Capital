from django.db import models
from django.conf import settings

class Transaction(models.Model):
    BANCO_CHOICES = [
        ('Nubank', 'Nubank'),
        ('Itaú', 'Itaú'),
        ('Bradesco', 'Bradesco'),
        ('Santander', 'Santander'),
        ('Banco do Brasil', 'Banco do Brasil'),
    ]
    
    CATEGORIA_CHOICES = [
        ('Alimentação', 'Alimentação'),
        ('Transporte', 'Transporte'),
        ('Lazer', 'Lazer'),
        ('Compras', 'Compras'),
        ('Saúde', 'Saúde'),
    ]
    
    TIPO_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Saída', 'Saída'),
    ]
    
    FORMA_CHOICES = [
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
        ('Transferência', 'Transferência'),
    ]

    STATUS_PAGAMENTO_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente')
    ]


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    banco = models.CharField(max_length=50, choices=BANCO_CHOICES)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    forma = models.CharField(max_length=20, choices=FORMA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.PositiveIntegerField(null=True, blank=True)
    descricao = models.TextField(max_length=300)
    data = models.DateField()
    status_pagamento = models.CharField(max_length=10, choices=STATUS_PAGAMENTO_CHOICES, default='Pendente')
    
    def __str__(self):
        return f"{self.tipo} - {self.banco} - R${self.valor}"
    
    def clean(self):
        """Validação personalizada que roda antes de salvar o modelo"""
        super().clean()
    
        if self.forma != 'Crédito' and self.status_pagamento == 'Pendente':
            self.status_pagamento = 'Pago'
        
    def save(self, *args, **kwargs):
        """Garante que as validações sejam executadas antes de salvar"""
        self.full_clean()
        super().save(*args, **kwargs)