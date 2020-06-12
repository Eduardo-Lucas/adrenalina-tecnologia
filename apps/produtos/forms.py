from django import forms

from apps.produtos.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'categoria', 'nome', 'foto', 'descricao', 'preco', 'preco_desconto',
            'saldo', 'disponivel'
        ]
