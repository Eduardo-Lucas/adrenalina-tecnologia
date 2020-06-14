from import_export import resources

from apps.financeiro.models import TipoPagamento, PrazoPagamento, TabelaPreco


class TipoPagamentoResource(resources.ModelResource):

    class Meta:
        model = TipoPagamento
        fields = '__all__'


class PrazoPagamentoResource(resources.ModelResource):

    class Meta:
        model = PrazoPagamento
        fields = '__all__'


class TabelaPrecoResource(resources.ModelResource):

    class Meta:
        model = TabelaPreco
        fields = '__all__'
