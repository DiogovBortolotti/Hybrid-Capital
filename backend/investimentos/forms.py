from django import forms
from .models import Investimento

class InvestimentoForm(forms.ModelForm):
    class Meta:
        model = Investimento
        fields = [
            'instituicao', 'tipo', 'nome_patrimonio', 
            'valor_cota', 'unidades', 'data_compra',
            'moeda', 'cotacao_dolar_pago', 'taxa_anual'
        ]
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date'}),
            'valor_cota': forms.NumberInput(attrs={'step': '0.01'}),
            'unidades': forms.NumberInput(attrs={'step': '0.000001'}),
            'cotacao_dolar_pago': forms.NumberInput(attrs={'step': '0.0001'}),
            'taxa_anual': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar campos opcionais obrigatórios apenas quando necessário
        self.fields['cotacao_dolar_pago'].required = False
        self.fields['taxa_anual'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        moeda = cleaned_data.get('moeda')
        cotacao_dolar_pago = cleaned_data.get('cotacao_dolar_pago')
        
        # Validar que cotacao_dolar_pago é obrigatório se moeda for USD
        if moeda == 'USD' and not cotacao_dolar_pago:
            self.add_error('cotacao_dolar_pago', 'Cotação do dólar é obrigatória para investimentos em USD')
        
        return cleaned_data