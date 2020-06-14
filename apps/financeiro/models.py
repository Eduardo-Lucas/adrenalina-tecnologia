from django.db import models
from django.urls import reverse

from apps.core.choices import SIM_NAO_CHOICES
from apps.empresas.models import Empresa


class TipoPagamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    codigo = models.CharField("Código Forma Pagamento", null=False, unique=True, max_length=3, default="DIN")
    descricao = models.CharField("Descrição Forma Pagamento", max_length=60, null=False, default=" ",
                                 help_text='Descrição Forma Pagamento para venda ou compra de produtos')
    habilitado = models.CharField("Tipo habilitado", max_length=60, null=False, default="S",
                                  choices=SIM_NAO_CHOICES,
                                  help_text='S para bloquear esta forma de pagamento nas vendas')
    negociada = models.CharField("Pode haver negociação", max_length=60, null=False, default="S",
                                 choices=SIM_NAO_CHOICES, help_text='S para permitir que vendedor possa negociar a '
                                                                    'forma de pagamento com cliente N- Não negocia')
    venda_parcelada = models.CharField("Pode haver parcelamento", max_length=60, null=False, default="S",
                                       choices=SIM_NAO_CHOICES, help_text='S para permitir que vendedor possa '
                                                                          'parcelar venda N- Não parcela')
    imprime_na_nfe = models.CharField("Imprimir dados na nota fiscal", max_length=60, null=False, default="S",
                                      choices=SIM_NAO_CHOICES, help_text='S para permitir que sistema imprima os '
                                                                         'dados financeiros na nfe / Danfe')
    habilitado_web = models.CharField("Habilita forma de pagamento na WEB", max_length=60, null=False, default="N",
                                      choices=SIM_NAO_CHOICES, help_text='S Habilita forma de pagamento na vendas '
                                                                         'via site WEB')
    # número de parcelas pré determinado para este pagamento - Se zeros, força que seja a vista
    num_parcelas = models.PositiveIntegerField("Numero de parcelas", null=False,
                                               help_text='Numero máximo de parcelas pre determinado para este '
                                                         'pagamento. Se zeros, força que seja a vista')
    prazos_padroes = models.CharField("Prazos padroes em dias", max_length=60, null=False, default="000",
                                      help_text='Informe os prazos padroes em numero de dias consecutivos de 3 em 3 '
                                                'ex 000030060090')

    # prazo em dias máximo pre determinado para este pagamento
    prazo_maximo = models.PositiveIntegerField("Prazo máximo em dias", null=False,
                                               help_text='Número máximo de prazo em dias pre determinado para '
                                                         'este pagamento')

    # tipo de documento será gerado para este tipo de venda
    # tipo_documento = models.ForeignKey(TipoDocumento, null=True, blank=True, on_delete=models.CASCADE)

    # Valor mínimo para este tipo de pagamento reverse
    valor_minimo = models.DecimalField("Valor mínimo para venda", max_length=16, max_digits=16, decimal_places=2,
                                       default=0.00, help_text='Valor mínimo para este tipo de pagamento reverse')

    # Valor máximo para este tipo de pagamento reverse
    valor_maximo = models.DecimalField("Valor máximo para venda", max_length=16, max_digits=16, decimal_places=2,
                                       default=0.00, help_text='Valor máximo para este tipo de pagamento reverse')

    class Meta:
        ordering = ('descricao',)
        verbose_name = 'Tipo de Pagamento'
        verbose_name_plural = 'Tipos de Pagamentos'

    def __str__(self):
        return self.descricao

    @staticmethod
    def get_absolute_url():
        return reverse('financeiro:tipopagamento_list')


# ----------------------------------------------------------------------------------------------------------------------
# PRAZOS DE PAGAMENTOS EXISTENTES NO SISTEMA (KCEITP)
# ----------------------------------------------------------------------------------------------------------------------
class PrazoPagamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    codigo = models.PositiveIntegerField(null=False, unique=True, )
    descricao = models.CharField(max_length=60, null=False)

    class Meta:
        ordering = ('codigo', )
        verbose_name = 'Prazo de Pagamento'
        verbose_name_plural = 'Prazos de Pagamentos'

    def __str__(self):
        return self.descricao

    @staticmethod
    def get_absolute_url():
        return reverse('financeiro:prazopagamento_list')


# todo Alinhar utilização da Tabela de Preços
class TabelaPreco(models.Model):
    descricao = models.CharField(max_length=50, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.descricao

    class Meta:
        ordering = ['descricao']
        unique_together = ['descricao', 'empresa']
        verbose_name = 'Tabela de Preço'
        verbose_name_plural = 'Tabelas de Preço'

    @staticmethod
    def get_absolute_url():
        return reverse('financeiro:tabelapreco_list')
