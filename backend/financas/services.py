# services.py
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.core.exceptions import ValidationError
from .models import Transaction, TransactionShare, SharedPayment
from django.conf import settings

from django.contrib.auth import get_user_model


class TransactionService:
    UserModel = get_user_model()

    @staticmethod
    def create_complete_transaction(owner, transaction_data, shares_data):
        """
        Cria uma transação completa com todos os compartilhamentos e pagamentos associados
        
        Args:
            owner: Usuário dono da transação
            transaction_data: Dicionário com dados da transação
            shares_data: Lista de dicionários com dados dos compartilhamentos
            
        Returns:
            Transaction: Objeto da transação criada
        """
        try:
            # Validação inicial
            if not owner or not isinstance(owner, TransactionService.UserModel):
                raise ValidationError("O dono da transação é obrigatório")
                
            if not transaction_data or 'valor' not in transaction_data:
                raise ValidationError("Dados da transação inválidos")
            
            # Cria a transação principal
            transaction = Transaction.objects.create(
                user=owner,
                **transaction_data
            )
            
            # Cria os compartilhamentos
            total_percentage = 0
            for share_data in shares_data:
                if 'shared_with' not in share_data:
                    continue
                    
                if share_data['shared_with'].id == owner.id:
                    continue  # Não compartilhar consigo mesmo
                    
                total_percentage += share_data.get('percentage', 0)
                TransactionShare.objects.create(
                    transaction=transaction,
                    **share_data
                )
            
            # Atualiza a porcentagem total compartilhada
            transaction.shared_percentage = total_percentage
            transaction.save()
            
            return transaction
            
        except Exception as e:
            # Rollback em caso de erro
            if 'transaction' in locals():
                transaction.delete()
            raise e

    @staticmethod
    def update_transaction_shares(transaction, shares_data):
        """
        Atualiza os compartilhamentos de uma transação existente
        
        Args:
            transaction: Objeto Transaction existente
            shares_data: Lista de dicionários com dados atualizados
            
        Returns:
            dict: Resumo das alterações
        """
        try:
            existing_shares = {s.id: s for s in transaction.shares.all()}
            updated_ids = set()
            total_percentage = 0
            
            # Processa cada compartilhamento
            for share_data in shares_data:
                share_id = share_data.get('id')
                
                if share_id and share_id in existing_shares:
                    # Atualiza compartilhamento existente
                    share = existing_shares[share_id]
                    for field, value in share_data.items():
                        setattr(share, field, value)
                    share.save()
                    updated_ids.add(share_id)
                    total_percentage += share.percentage
                else:
                    # Cria novo compartilhamento
                    if 'shared_with' in share_data and share_data['shared_with'].id != transaction.user.id:
                        share = TransactionShare.objects.create(
                            transaction=transaction,
                            **share_data
                        )
                        total_percentage += share.percentage
                        updated_ids.add(share.id)
            
            # Remove compartilhamentos não enviados
            deleted_ids = set(existing_shares.keys()) - updated_ids
            if deleted_ids:
                TransactionShare.objects.filter(id__in=deleted_ids).delete()
            
            # Atualiza porcentagem total
            transaction.shared_percentage = total_percentage
            transaction.save()
            
            return {
                'updated': len(updated_ids),
                'created': len(updated_ids) - len(existing_shares),
                'deleted': len(deleted_ids)
            }
            
        except Exception as e:
            raise e

    @staticmethod
    def get_user_financial_summary(user):
        """
        Obtém um resumo financeiro completo para o usuário
        
        Args:
            user: Usuário para o qual obter o resumo
            
        Returns:
            dict: Dicionário com o resumo financeiro
        """
        # Como dono de transações
        owned_summary = Transaction.objects.filter(user=user).aggregate(
            total_value=Sum('valor'),
            total_shared=Sum('shared_payment'),
            total_owner_part=Sum('owner_payment'),
            count=Sum('id', distinct=True)
        )
        
        # Como participante em compartilhamentos
        shared_summary = TransactionShare.objects.filter(shared_with=user).aggregate(
            total_value=Sum(F('transaction__valor') * F('percentage') / 100),
            total_installments=Sum('installments'),
            count=Sum('id', distinct=True)
        )
        
        # Pagamentos pendentes
        pending_payments = SharedPayment.objects.filter(
            transaction_share__shared_with=user,
            status='Pendente'
        ).aggregate(
            total=Sum('amount'),
            count=Sum('id', distinct=True)
        )
        
        # Pagamentos a receber
        payments_to_receive = SharedPayment.objects.filter(
            transaction_share__transaction__user=user,
            status='Pendente'
        ).aggregate(
            total=Sum('amount'),
            count=Sum('id', distinct=True)
        )
        
        return {
            'as_owner': {
                'total_transactions': owned_summary.get('count', 0),
                'total_value': owned_summary.get('total_value', 0),
                'total_shared': owned_summary.get('total_shared', 0),
                'total_owner_part': owned_summary.get('total_owner_part', 0)
            },
            'as_shared': {
                'total_transactions': shared_summary.get('count', 0),
                'total_value': shared_summary.get('total_value', 0),
                'total_installments': shared_summary.get('total_installments', 0)
            },
            'pending_payments': {
                'total': pending_payments.get('total', 0),
                'count': pending_payments.get('count', 0)
            },
            'payments_to_receive': {
                'total': payments_to_receive.get('total', 0),
                'count': payments_to_receive.get('count', 0)
            },
            'net_balance': (
                (owned_summary.get('total_owner_part', 0) + 
                payments_to_receive.get('total', 0)) - 
                pending_payments.get('total', 0)
            )
        }

    @staticmethod
    def process_payment(payment_id, paid_by_user, payment_date=None, amount=None):
        """
        Processa um pagamento compartilhado
        
        Args:
            payment_id: ID do SharedPayment
            paid_by_user: Usuário que está realizando o pagamento
            payment_date: Data do pagamento (opcional)
            amount: Valor pago (opcional, usa o valor original se não informado)
            
        Returns:
            SharedPayment: Objeto do pagamento processado
        """
        try:
            payment = SharedPayment.objects.get(id=payment_id)
            
            if payment.status == 'Pago':
                raise ValidationError("Este pagamento já foi realizado")
                
            payment.status = 'Pago'
            payment.paid_by = paid_by_user
            payment.payment_date = payment_date or date.today()
            
            if amount is not None:
                payment.amount = amount
                
            payment.save()
            return payment
            
        except SharedPayment.DoesNotExist:
            raise ValidationError("Pagamento não encontrado")

    @staticmethod
    def cancel_payment(payment_id, reason=None):
        """
        Cancela um pagamento compartilhado
        
        Args:
            payment_id: ID do SharedPayment
            reason: Motivo do cancelamento (opcional)
            
        Returns:
            SharedPayment: Objeto do pagamento cancelado
        """
        try:
            payment = SharedPayment.objects.get(id=payment_id)
            
            if payment.status == 'Pago':
                raise ValidationError("Não é possível cancelar um pagamento já realizado")
                
            payment.status = 'Cancelado'
            payment.save()
            return payment
            
        except SharedPayment.DoesNotExist:
            raise ValidationError("Pagamento não encontrado")

    @staticmethod
    def check_overdue_payments():
        """
        Verifica e atualiza pagamentos atrasados
        """
        today = date.today()
        overdue_payments = SharedPayment.objects.filter(
            status='Pendente',
            due_date__lt=today
        ).update(status='Atrasado')
        
        return overdue_payments

    @staticmethod
    def get_transaction_payment_plan(transaction_id):
        """
        Obtém o plano de pagamento completo para uma transação
        
        Args:
            transaction_id: ID da transação
            
        Returns:
            dict: Estrutura com detalhes do plano de pagamento
        """
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            shares = transaction.shares.all().select_related('shared_with')
            
            payment_plan = {
                'transaction': {
                    'id': transaction.id,
                    'description': transaction.descricao,
                    'total_value': transaction.valor,
                    'owner_value': transaction.owner_payment,
                    'shared_value': transaction.shared_payment
                },
                'shares': []
            }
            
            for share in shares:
                payments = share.payments.all().order_by('installment_number')
                share_data = {
                    'user': {
                        'id': share.shared_with.id,
                        'name': share.shared_with.get_full_name()
                    },
                    'percentage': share.percentage,
                    'total_shared_value': share.total_shared_value,
                    'installments': []
                }
                
                for payment in payments:
                    share_data['installments'].append({
                        'id': payment.id,
                        'due_date': payment.due_date,
                        'amount': payment.amount,
                        'status': payment.status,
                        'payment_date': payment.payment_date,
                        'installment_number': payment.installment_number
                    })
                
                payment_plan['shares'].append(share_data)
            
            return payment_plan
            
        except Transaction.DoesNotExist:
            raise ValidationError("Transação não encontrada")