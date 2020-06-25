from django import forms
from django.forms import inlineformset_factory

from apps.clientes.models import Cliente
from apps.pedidos.models import Pedido, PedidoItem


class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ['cliente', 'loja', 'mesa', 'pedidostatus', 'tipo_de_pagamento', 'prazo_de_pagamento']


class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = (
            'produto', 'quantidade', 'preco_unitario', 'total_produto',
        )
        # fields = (
        #     'produto', 'preco_venda', 'quantidade', 'total_produto',
        # )
        exclude = ('pedidoweb', 'sequencia', 'unidade', 'descricao', 'observacoes',
                   'cfop', 'codigo_ncm', 'codigo_cest', 'status_pedido_item', 'autorizacao_faturamento',
                   'autorizacao_numitem', 'peso_liquido', 'peso_bruto', 'metro_cubico', 'movimenta_estoques',
                   'saldo_fisico', 'saldo_fiscal', 'preco_custo', 'preco_medio', 'preco_custo_nfe', 'preco_medio_nfe',
                   'perc_desc', 'custo_informado', 'data_movimento', 'modalidade_ipi',
                   'situacao_tributaria_ipi', 'base_calc_ipi', 'perc_ipi', 'perc_red_ipi', 'modalidade_calculo',
                   'modalidade_icms', 'situacao_tributaria_icms', 'base_calc_icms', 'perc_icms',
                   'perc_antec_tributaria', 'perc_red_icms', 'modalidade_calculo_subst', 'base_calc_icms_sub',
                   'perc_mva_sub', 'perc_icms_sub', 'perc_reducao_icms_sub', 'base_calc_antecipacao_trib',
                   'perc_antecipacao_trib', 'situacao_tributaria_pis', 'base_calc_pis', 'perc_pis',
                   'situacao_tributaria_cofins', 'base_calc_cofins', 'perc_fundo_pobreza', 'perc_trib_aproximado',
                   'base_calc_import', 'perc_import', 'base_calc_issqn', 'perc_issqn', 'perc_desp_acessorias',
                   'perc_seguro', 'perc_frete', 'natureza_custos', 'centro_custo', 'codigo_promocao',
                   'ultima_alteracao', )


PedidoItemFormSet = inlineformset_factory(Pedido, PedidoItem,
                                          form=PedidoItemForm, extra=1)
