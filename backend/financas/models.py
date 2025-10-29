from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from dateutil.relativedelta import relativedelta

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
        ('Casa', 'Casa'),
        ('Carro', 'Carro'),
        ('Assinatura', 'Assinatura'),
        ('Estudo', 'Estudo'),
        ('Salario', 'Salario'),
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
        verbose_name='Usuário',
        related_name='transactions_created'
    )
    banco = models.CharField(max_length=50, choices=BANCO_CHOICES)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    forma = models.CharField(max_length=20, choices=FORMA_CHOICES)
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    parcelas = models.PositiveIntegerField(
        null=True, 
        blank=True,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(24)]
    )
    descricao = models.TextField(max_length=300)
    data = models.DateField(default=date.today, null=False)
    status_pagamento = models.CharField(
        max_length=10, 
        choices=STATUS_PAGAMENTO_CHOICES, 
        default='Pendente'
    )
    shared_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name='Porcentagem total compartilhada',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data', '-created_at']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'


    def mark_as_paid(self, payment_date=None):
        """
        Marca a transação como paga.
        Se não passar payment_date, usa a data/hora atual.
        """
        if self.status_pagamento != 'Pago':
            self.status_pagamento = 'Pago'
            self.paid_at = payment_date or timezone.now()
            self.save()

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
    
    @property
    def owner_payment(self):
        """Calcula o valor que o dono deve pagar"""
        return self.valor * (100 - self.shared_percentage) / 100
    
    @property
    def shared_payment(self):
        """Calcula o valor total compartilhado"""
        return self.valor * self.shared_percentage / 100
    
    def create_shares(self, shares_data):
        """Cria os compartilhamentos para esta transação"""
        from .services import TransactionService
        return TransactionService.create_shares_for_transaction(self, shares_data)

class TransactionShare(models.Model):
    transaction = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
        related_name='shares'
    )
    shared_with = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shared_transactions'
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Porcentagem compartilhada',
        validators=[MinValueValidator(0.01), MaxValueValidator(100)]
    )
    installments = models.PositiveIntegerField(
        default=1,
        verbose_name='Número de parcelas',
        validators=[MinValueValidator(1), MaxValueValidator(24)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('transaction', 'shared_with')
        verbose_name = 'Compartilhamento'
        verbose_name_plural = 'Compartilhamentos'

    def __str__(self):
        return f"{self.percentage}% de R${self.transaction.valor} para {self.shared_with.get_full_name()}"
    
    def save(self, *args, **kwargs):
        """Valida e cria os pagamentos compartilhados"""
        self.full_clean()
        created = not self.pk
        super().save(*args, **kwargs)
        
        if created:
            self.create_shared_payments()
    
    def create_shared_payments(self):
        """Cria os pagamentos compartilhados para este compartilhamento"""
        SharedPayment.create_for_transaction_share(self)
    
    @property
    def total_shared_value(self):
        """Retorna o valor total compartilhado"""
        return self.transaction.valor * self.percentage / 100
    
    @property
    def installment_value(self):
        """Retorna o valor de cada parcela"""
        return self.total_shared_value / self.installments

class SharedPayment(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]

    transaction_share = models.ForeignKey(
        'TransactionShare',
        on_delete=models.CASCADE,
        related_name='payments'
    )
    payment_date = models.DateField(
        verbose_name='Data do pagamento',
        null=True,
        blank=True
    )
    due_date = models.DateField(
        verbose_name='Data de vencimento'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor da parcela'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pendente'
    )
    installment_number = models.PositiveIntegerField(
        verbose_name='Número da parcela'
    )
    paid_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments_made'
    )
    received_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments_received'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date', 'installment_number']
        verbose_name = 'Pagamento Compartilhado'
        verbose_name_plural = 'Pagamentos Compartilhados'
        unique_together = ('transaction_share', 'installment_number')

    def __str__(self):
        return f"Parcela {self.installment_number} de {self.transaction_share} - {self.status}"

    @classmethod
    def create_for_transaction_share(cls, transaction_share):
        """Cria todas as parcelas para um compartilhamento"""
        payments = []
        
        for i in range(1, transaction_share.installments + 1):
            payments.append(cls(
                transaction_share=transaction_share,
                due_date=date.today() + relativedelta(months=i-1),
                amount=transaction_share.installment_value,
                installment_number=i,
                received_by=transaction_share.transaction.user,
                status='Pendente'
            ))
        
        cls.objects.bulk_create(payments)
        return payments
    
    def mark_as_paid(self, paid_by_user, payment_date=None):
        """Marca o pagamento como realizado"""
        self.status = 'Pago'
        self.paid_by = paid_by_user
        self.payment_date = payment_date or date.today()
        self.save()