from django import forms
from django.forms import inlineformset_factory

from apps.caixas.models import CaixaMovimento, Caixa


class CaixaMovimentoForm(forms.ModelForm):
    class Meta:
        model = CaixaMovimento
        fields = (
            'tipopagamento', 'valor_movimento', 'entrada_saida', 'observacao'
        )


CaixaMovimentoFormSet = inlineformset_factory(Caixa, CaixaMovimento,
                                              form=CaixaMovimentoForm, extra=1)
