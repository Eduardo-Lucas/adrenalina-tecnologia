from django.contrib.auth.models import User
from django.db import models


# ----------------------------------------------------------------------------------------------------------------------
# PEDIDOS DE VENDAS ORÇAMENTOS ENCOMENDAS REQUISIÇÕES ETC (KCEI03)
# ----------------------------------------------------------------------------------------------------------------------
from django.urls import reverse

from apps.clientes.models import Cliente
from apps.core.choices import SIM_NAO_CHOICES
from apps.empresas.models import Empresa
from apps.financeiro.models import TipoPagamento, PrazoPagamento
from apps.lojas.models import Loja
from apps.produtos.models import Produto


class Mesa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(default=1, unique=True)
    aberta = models.BooleanField(default=True,
                                 help_text='A mesa tem que estar aberta para constar no Pedido')

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return str(self.numero)

    @staticmethod
    def get_absolute_url():
        return reverse('pedidos:mesa_list')


class PedidoStatus(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['descricao', ]

    def __str__(self):
        return self.descricao


class Pedido(models.Model):
    # id do será o Número do pedido
    # Série será as 3 primeiras letras do Código da empresa
    # subserie conforme operação "VEN" "ORC" "DEV"=DEVOLUÇÃO "ETC"
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.CASCADE,  )
    loja = models.ForeignKey(Loja, default=1, on_delete=models.CASCADE,  )
    mesa = models.ForeignKey(Mesa, null=True, blank=True, on_delete=models.SET_NULL)
    serie = models.CharField(max_length=3, null=False, default='MAT')
    subserie = models.CharField(max_length=3, null=False, default='VEN')

    # informação deve ser trazida da tabela TipoDocumento
    indicador_pagamento_nfe = models.CharField("Indicador da forma de pagamento", max_length=1, null=False, default="0",
                                               help_text='Indicador da forma de pagamento para informação na nota '
                                                         'fiscal eletrônica')

    status_pedido = models.ForeignKey(PedidoStatus, max_length=50,
                                      on_delete=models.CASCADE, default='Pedido')

    # Código do regime Tributário do emitente ou do fornecedor 1-Simples na 2-Simples exc  3-Normal
    regime_tributario = models.CharField("Regime Tributário Emitente", max_length=1, null=False, default="1",

                                         help_text='código do regime tributário do emitente ou do fornecedor '
                                                   '1-Simples na 2-Simples exc  3-Normal')

    # notafiscal = models.ForeignKey('faturamento.NotaFiscal', on_delete=models.CASCADE, null=True, blank=True,
    #                                help_text='Número da nota fiscal emitida para este pedido conforme Número no '
    #                                          'faturamento da NFe ou NFce')

    # Número da autorização para Faturamento
    autorizacao_faturamento = models.CharField("Número da autorização para Faturamento", max_length=20, null=True,
                                               blank=True, help_text='Número da autorização de faturamento emitida '
                                                                     'pelo cliente ou pelo fornecedor')

    autorizacao_numitem = models.PositiveIntegerField("Número do Pedido", default=0)

    # Indicador de emitente do documento fiscal
    indicador_emitente = models.CharField("Indicador de emitente da NFe", max_length=1, null=True,
                                          default="1",
                                          help_text='Indicador de emitente do documento fiscal  0_Emissão própria '
                                                    '1_Terceiros')

    # 00|Doc regular| 01|Doc reg extemporâneo| 02|Doc cancelado|  03|Doc canc extemporâneo| 04|NFe denegada|
    # 05|NFe Numeração inutilizada| 06|Doc Fiscal Compl| 07|Doc Fiscal Compl extemporâneo| 08|Doc RegEspecial
    # Situação da nota fiscal quanto ao cancelamento (item 4.1.2- Tabela Situação do Documento do AtoCOTEPE/ICMS nº 09,
    #  de 2008),
    # situacaodocumentosped = models.ForeignKey(SituacaoDocumentoSped, on_delete=models.CASCADE, null=False, default=1,
    #                                           help_text='Situação Do Documento Fiscal conforme tabela 4.1.2 do Sped')

    situacaodocumentosped = models.PositiveIntegerField(default=1)

    # TODO  Depois tem que mudar para 55
    modelodocumentofiscal = models.PositiveIntegerField(default=1)

    # modelodocumentofiscal = models.ForeignKey(ModeloDocumentoFiscal, on_delete=models.CASCADE, null=False, default=1,
    #                                           help_text='Código Do Documento Fiscal conforme tabela Sped -
    # Ex. 55|Nota'
    #                                                     ' Fiscal Eletrônica')

    data_pedido = models.DateField('Data do Pedido', null=False, blank=False, auto_now_add=True)
    data_emissao = models.DateField('Data de De Emissão da Nfe', null=False, blank=False, auto_now_add=True)
    data_saida = models.DateTimeField('Data de saida para entrega', null=False, blank=False, auto_now_add=True)
    data_movimento = models.DateTimeField('Data de Movimentação da Nfe', null=False, blank=False, auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    # natureza da operação fiscal de base  ou cfop principal que indicará o tipo de saida (nos itens tem vários)
    # TODO Takes out null=True e blank=True
    # cfop = models.ForeignKey(Cfop, on_delete=models.CASCADE, blank=True, null=True,
    #                         help_text='Informe o Cfop - Código fiscal de Operação')

    # tipo de pagamento utilizado neste pedido
    tipo_de_pagamento = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE, default=1,
                                          related_name='tipopagamentoWeb')

    # Prazos para pagamento
    prazo_de_pagamento = models.ForeignKey(PrazoPagamento, on_delete=models.CASCADE, default=1)

    # Código do participante (Cliente Web) nesta operação fiscal
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # vendedor responsável pela venda ou comprador
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendedor')

    # mensagem padrao a ser impressa durante a emissão da nota fiscal como observações adicionais na NF
    # mensagempadrao = models.ForeignKey(MensagemPadrao, on_delete=models.CASCADE, null=True,
    #                                   help_text='mensagem padrão a ser impressa durante a emissão da nota fiscal '
    #                                             'como observações adicionais na NF')

    # Tipo de movimentação de entrada ou saida
    # TODO Depois tornar preenchimento obrigatório
    tipo_pedido = models.CharField(max_length=10, default='saida', )
    # help_text='Informe entrada ou saida de Produto')

    # indPres (nfe 3.10) Indicador de presença do comprador no estabelecimento ----
    indicador_presenca_nfe = models.CharField("Indicador de presença do comprador NFe", max_length=1, null=False,
                                              default="1",
                                              help_text='indPres (nfe 3.10) Indicador de presença do comprador no '
                                                        'estabelecimento comercial no momento da operação')

    # Tipo de Preço usado na saida de pedidos da tabela
    tipo_preco_pedido = models.CharField(max_length=1, null=False, default="V",
                                         help_text='Tipo de Preço usado na saida de pedidos V Preço VENDA / '
                                                   'C Último CUSTO / I Preço indexado, etc')

    # Total bruto (sem descontos) dos  produtos no pedido
    total_produtos = models.DecimalField("Total dos Produtos", max_length=16, max_digits=16, decimal_places=2,
                                         default=0.00, help_text='Total bruto (sem descontos) dos  produtos no '
                                                                 'pedido')
    # Percentual  % desconto total na Nf para rateio por item nos itens
    perc_desc = models.DecimalField("Percentual de descontos nos produtos", max_length=10, max_digits=10,
                                    decimal_places=6, default=0.00, help_text='Percentual de descontos nos produtos')
    # valor do desconto na nota fiscal em totais (valor dos descontos em % + valor dos descontos em valores do pedido)
    descont_valor = models.DecimalField("Valor desconto no Pedido", max_length=16, max_digits=16, decimal_places=2,
                                        default=0.00, help_text='valor do desconto na nota fiscal em totais (valor dos '
                                                                'descontos em % + valor dos descontos em valores do '
                                                                'pedido')

    # valores de cálculo do IPI
    base_calc_ipi = models.DecimalField("Base de cálculo do IPI", max_length=16, max_digits=16, decimal_places=2,
                                        default=0.00, help_text='Base de cálculo do IPI')
    valor_ipi = models.DecimalField("Valor do IPI", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                    help_text='Valor calculado do IPI a recolher.')
    perc_ipi = models.DecimalField("Percentual do IPI", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                   help_text='Percentual do IPI a recolher.')

    # Total líquido do pedido (somatório dos produtos - descontos + impostos + frete + outros valores)
    valor_contabil = models.DecimalField("Total líquido do Pedido", max_length=16, max_digits=16, decimal_places=2,
                                         default=0.00,
                                         help_text='Total líquido do pedido/total líquido da Nota fiscal pedido.')

    base_calc_icms = models.DecimalField("Base de cálculo do ICMS", max_length=16, max_digits=16, decimal_places=2,
                                         default=0.00, help_text='Base de cálculo do ICMS.')
    valor_icms = models.DecimalField("Valor do ICMS", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                     help_text='Valor calculado do ICMS a recolher.')
    perc_icms = models.DecimalField("Percentual do ICMS", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                    help_text='Percentual do ICMS a recolher.')

    # valores de cálculo do ICMS substituição tributária
    # valor do icms a recolher calculado=valor_icms_sub - valor_icms
    base_calc_icms_sub = models.DecimalField("Base de cálculo do Icms Substituição", max_length=16,
                                             max_digits=16, decimal_places=2, default=0.00,
                                             help_text='Base de cálculo do Icms Substituição tributária')
    valor_icms_sub = models.DecimalField("Valor do ICMS substituição tributária", max_length=16,
                                         max_digits=16, decimal_places=2, default=0.00,
                                         help_text='Valor do ICMS substituição tributária')

    # valor das despesas acessórias para rateio por item
    valor_despesas_acess = models.DecimalField("Valor despesas acessorias", max_length=16,
                                               max_digits=16, decimal_places=2, default=0.00,
                                               help_text='Valor das despesas acessorias')

    # valor do pis para rateio por item
    base_calc_pis = models.DecimalField("Valor Base de cálculo do Pis", max_length=16,
                                        max_digits=16, decimal_places=2, default=0.00,
                                        help_text='Valor Base de cálculo do Pis')

    valor_pis = models.DecimalField("Valor do Pis", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                    help_text='Valor do pis')

    # valor do cofins para rateio por item
    base_calc_cofins = models.DecimalField("Valor Base de cálculo do cofins", max_length=16,
                                           max_digits=16, decimal_places=2, default=0.00,
                                           help_text='Valor Base de cálculo do cofins')
    valor_cofins = models.DecimalField("Valor do cofins", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                       help_text='Valor do cofins')

    # valor do seguro
    valor_seguro = models.DecimalField("Valor do cofins", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                       help_text='Valor do cofins')

    # valor dos serviços se nfe for de serviços
    base_calc_issqn = models.DecimalField("Base de cálculo serviços", max_length=16,
                                          max_digits=16, decimal_places=2, default=0.00,
                                          help_text='valor Base de cálculo serviços se nfe for de serviços')
    perc_issqn = models.DecimalField("Percentual do ISS", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                     help_text='Percentual do ISS a recolher.')
    quantidade_servicos = models.DecimalField("Quantidade de serviços", max_length=10,
                                              max_digits=10, decimal_places=6, default=0.00,
                                              help_text='Quantidade dos serviços se nfe for de serviços')
    valor_servicos = models.DecimalField("Valor dos serviços", max_length=16, max_digits=16,
                                         decimal_places=2, default=0.00,
                                         help_text='valor dos serviços se nfe for de serviços')

    # valor do frete neste operação fiscal e Código da transportadora
    # transportadora = models.ForeignKey(Participante, on_delete=models.CASCADE, null=True, blank=True,
    #                                    related_name='transportadoraWeb',
    #                                    help_text='Código da transportadora nesta operação fiscal')
    valor_frete = models.DecimalField("Valor do FRETE", max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                      help_text='Valor do frete na nota fiscal de entrada ou de saida')
    valor_icm_frete = models.DecimalField("Valor do icms sobre o frete", max_length=16, max_digits=16,
                                          decimal_places=2, default=0.00,
                                          help_text='Valor do icms sobre o frete na nota fiscal de entrada ou de saida')
    cif_fob_frete = models.CharField("Indicador do tipo de frete", max_length=1, null=False, default="1",

                                     help_text='Indicador de frete. 0-Emitente, 1-Destinatário , 2-Terceiros, 3-Próprio'
                                               ' remetente, 4-próprio destinatário, 9-Sem')
    tipo_frete = models.CharField("Indicador do custo do frete", max_length=1, null=False, default="1",

                                  help_text='1 Frete na NFe COM cre 2-Incluso na Nfe sem crédito 3-Conhec a parte '
                                            '4-Conhec parte sem cred')

    status_manifestacao = models.CharField(max_length=1, null=False, default="C",

                                           help_text='Status de conferencia na manifestação de destinatário para efeito'
                                                     ' de liberação de produtos para venda')

    status_contabilidade = models.CharField(max_length=1, null=False, default="C",

                                            help_text='Status de conferencia da NF  pela contabilidade informando que '
                                                      'nf está fiscalmente OK')

    status_financeiro = models.CharField(max_length=1, null=False, default="A",

                                         help_text='Status de conferencia da NF  pelo departamento financeiro '
                                                   'informando que nf está financeiramente (contas a pagar) OK')

    status_precos = models.CharField(max_length=1, null=False, default="C",

                                     help_text='Status de conferencia da NF  pelo departamento custos informando que '
                                               'nf está com preços e custos OK')

    status_expedicao = models.CharField(max_length=1, null=False, default="L",
                                        help_text='Status de conferencia da NF  pela expedição informando que nf está '
                                                  'com quantidades armazenadas OK')
    # "S" para que nf esteja totalizada OK  E SEM DIFERENCA
    # "D" para NF com diferenca e com saldo não atualizado

    status_diferenca = models.CharField(max_length=1, null=False, default="C",

                                        help_text='Status de conferencia dos valores na nota fiscal de entrada ou '
                                                  'saida para ver se há diferenças ')

    observacoes = models.TextField("Observações", max_length=200, null=True, blank=True)
    ultima_alteracao = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('pedidos:pedido_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)
        # return str(self.id) + ' ' + str(self.serie) + ' ' + str(self.subserie)

    def total_preco_unitario(self):
        return str(sum(pedidoitem.tot_preco_unitario() for pedidoitem in self.items.all()))

    def total_desconto(self):
        return str(sum(
            pedidoitem.valor_desconto() for pedidoitem in self.items.all()
        )
        )

    def maior_sequencia(self):
        return str(max(pedidoitem.sequencia for pedidoitem in self.items.all()))

    def total_preco_bruto(self):
        return str(sum(pedidoitem.total_preco_bruto() for pedidoitem in self.items.all()))

    def total_preco_liquido(self):
        return str(sum(
            pedidoitem.total_preco_bruto() for pedidoitem in self.items.all()) -
                   sum(pedidoitem.valor_desconto() for pedidoitem in self.items.all())
                   )

    def pode_alterar_pedido(self):
        if self.status_pedido == 'W':
            return True
        else:
            return False

    class Meta:
        ordering = ['-id']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


# ------------------------------------------------------------------------------------------------------------------
# itens do pedido
# ------------------------------------------------------------------------------------------------------------------
class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    sequencia = models.PositiveIntegerField("Sequência do item", null=False, default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    unidade = models.CharField(max_length=13, null=False, default="UN",
                               help_text='Unidade do produto vendido conforme cadastro no momento da venda. A mesma '
                                         'do cadastro de produtos')

    descricao = models.CharField(max_length=60, null=False, default="Descricao",
                                 help_text='Descrição do produto vendido conforme cadastro no momento da venda. A '
                                           'mesma do cadastro de produtos')

    observacoes = models.CharField(max_length=40, null=True, blank=True, default=" ",
                                   help_text='Observação para efeito de informação fiscal específica neste produto')

    # natureza da operação fiscal de base  ou cfop que indicará o tipo de operação
    # (cfop+data) (data+cfop)
    # TODO CFOP Resolver depois
    # cfop = models.ForeignKey(Cfop, on_delete=models.CASCADE, default=1,
    #                         help_text='natureza de operação fiscal específica deste produto')
    cfop = models.IntegerField(default=5102)

    # TODO CFOP Resolver depois
    # codigo_ncm = models.ForeignKey(CodigoNcm, on_delete=models.CASCADE, default=1)
    codigo_ncm = models.CharField(max_length=100, default=0)

    # TODO CFOP Resolver depois
    # codigo_cest = models.ForeignKey(CodigoCest, on_delete=models.CASCADE, default=1)
    codigo_cest = models.IntegerField(default=0)

    # Orçamento / Devolução / Cancelado / Em análise crédito/ Bloqueado/ Faturado / quitado etc
    status_pedido_item = models.CharField("Status deste pedido", max_length=1, null=False, default="N",

                                          help_text='status do pedido Orçamento / Devolução /Cancelado /Em análise '
                                                    'crédito /Bloqueado/ Faturado / quitado etc ')

    # Número da autorização para Faturamento
    autorizacao_faturamento = models.CharField("Número da autorização para Faturamento", max_length=20,
                                               null=True, blank=True,
                                               help_text='Número da autorização de faturamento emitida pelo cliente '
                                                         'ou pelo fornecedor')
    autorizacao_numitem = models.PositiveIntegerField("Número do Pedido", default=0,
                                                      )

    quantidade = models.DecimalField("Quantidade", max_length=16, max_digits=16, decimal_places=0,
                                     default=1,)
    # help_text='Quantidade vendida de produtos no pedido e nota fiscal de entrada ou '
    #          'de saida')

    peso_liquido = models.DecimalField("Peso líquido do produto", max_length=16, max_digits=16, decimal_places=6,
                                       default=0.00, help_text='peso líquido deste produto')
    peso_bruto = models.DecimalField("Peso bruto do produto", max_length=16, max_digits=16, decimal_places=6,
                                     default=0.00, help_text='peso bruto deste produto')

    metro_cubico = models.DecimalField("metros cúbicos do produto", max_length=16, max_digits=16, decimal_places=6,
                                       default=0.00, help_text='metros cúbicos do produto')

    # movimenta estoques - campo trazido do cadastro de CFOP mas que pode ser alterado
    # campo com "N" sempre que a n nota fiscal estiver bloqueada para análise
    movimenta_estoques = models.CharField("Movimenta Estoques?", max_length=3, null=False, default="Não",
                                          choices=SIM_NAO_CHOICES, help_text='S para movimentar estoques e N para nao '
                                                                             'movimentar')

    saldo_fisico = models.DecimalField("Saldo físico do produto após gravação do pedido", max_length=16, max_digits=16,
                                       decimal_places=6, default=0.00, help_text='Saldo físico do produto após '
                                                                                 'gravação')

    saldo_fiscal = models.DecimalField("Saldo físico do produto após gravação", max_length=16, max_digits=16,
                                       decimal_places=6, default=0.00, help_text='Saldo fiscal do produto após '
                                                                                 'geração e gravação da nota fiscal '
                                                                                 'emitida ou recebida')

    preco_custo = models.DecimalField("Preço de custo calculado após gravação", max_length=16, max_digits=16,
                                      decimal_places=6, default=0.00,
                                      help_text='Preço de custo do produto após gravação da nota fiscal de entrada '
                                                'ou saida')
    preco_venda = models.DecimalField("Preço de Venda", max_length=16, max_digits=16,
                                      decimal_places=2, default=0.00,
                                      help_text='Preço de Venda')
    preco_medio = models.DecimalField("Preço de custo médio calculado após gravação", max_length=16, max_digits=16,
                                      decimal_places=6, default=0.00,
                                      help_text='Preço de custo médio do produto após gravação da nota fiscal de '
                                                'entrada ou saida')
    preco_custo_nfe = models.DecimalField("Preço de custo calculado após gravação da NFe", max_length=16, max_digits=16,
                                          decimal_places=6, default=0.00,
                                          help_text='Preço de custo do produto após gravação da nota fiscal de '
                                                    'entrada ou saida')
    preco_medio_nfe = models.DecimalField("Preço de custo médio calculado após gravação da Nfe", max_length=16,
                                          max_digits=16, decimal_places=6, default=0.00,
                                          help_text='Preço de custo médio do produto após gravação a nota fiscal de '
                                                    'entrada ou saida')

    preco_unitario = models.DecimalField("Preço Unitário", max_length=16, max_digits=16,
                                         decimal_places=6, default=0.00,
                                         help_text='Preço unitário de venda conforme negociação e configurações do '
                                                   'sistema')
    perc_desc = models.DecimalField("% Desc", max_length=10, max_digits=10,
                                    decimal_places=6, default=0.00, help_text='Percentual de descontos nos produtos')

    custo_informado = models.DecimalField("Preço gerencial de venda", max_length=16, max_digits=16,
                                          decimal_places=6, default=0.00,
                                          help_text='Preço gerencial de venda conforme negociação para efeito de '
                                                    'cálculo de Preço de venda')

    # data de movimento lembrar (codigo + data) e (data+codigo) servirão para diversas operações no sistema
    data_movimento = models.DateTimeField('Data de Movimentação do produto', null=False, blank=False, auto_now_add=True,
                                          help_text='Data de Movimentação do produto. Mesma data do pedido para '
                                                    'efeito de cálculo de saldos (Codigo+data)')
    # Código do participante (Cliente ou fornecedor) nesta operação fiscal -
    # participante+data) (data+participante) (participante+codigo) (codigo+participante)- relatórios extratos
    # participante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clienteItem',
    #                                  blank=True, null=True)
    # participante = models.ForeignKey('faturamento.Participante', on_delete=models.CASCADE,
    # related_name='fornecedoresWeb',
    # blank=True, null=True, help_text='Código do Participante')

    # Total bruto (sem descontos) dos  produtos no pedido
    total_produto = models.DecimalField("Total do Produto", max_length=16, max_digits=16, decimal_places=2,
                                        default=0.00, help_text='Total bruto (sem descontos) do produto no pedido')

    # valores de cálculo do IPI  - indicação de tributação  de IPI 1=trib 2=Isento ou não trib 3=
    modalidade_ipi = models.CharField("Modalidade de cálculo do IPI ?", max_length=1, null=False, default="1",
                                      help_text='Modalidade de cálculo da base Icms')
    # TODO Resolver depois
    # situacao_tributaria_ipi = models.ForeignKey(SituacaoTribIpi, on_delete=models.CASCADE, default=1,
    #                                             help_text='Código da situação tributária quanto ao pis nesta
    # operação fiscal')
    situacao_tributaria_ipi = models.IntegerField(default=1)
    base_calc_ipi = models.DecimalField("Base de cálculo do IPI", max_length=16, max_digits=16, decimal_places=2,
                                        default=0.00,
                                        help_text='Base de cálculo do IPI=valor produtos - descontos')
    perc_ipi = models.DecimalField("Percentual do IPI", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                   help_text='Percentual do IPI a recolher.')
    perc_red_ipi = models.DecimalField("Percentual de redução de base do IPI", max_length=10, max_digits=10,
                                       decimal_places=6, default=0.00,
                                       help_text='Percentual de redução de base do IPI.')

    # 3 valor da operação/0 Margem Valor Agregado(%)/1 Pauta (Valor)/2 Preço Tabelado Máx.(valor)
    modalidade_calculo = models.CharField("Modalidade de cálculo da base Icms?", max_length=1, null=False, default="3",

                                          help_text='Modalidade de cálculo da base Icms')

    # indicação de tributação de ICMS 1=tributado 2=Isento ou não tributado 3=
    modalidade_icms = models.CharField("Modalidade de cálculo da base Icms?", max_length=1, null=False, default="3",
                                       help_text='Modalidade de cálculo da base Icms')

    # TODO Resolver depois
    # situacao_tributaria_icms = models.ForeignKey(SituacaoTribIcms, on_delete=models.CASCADE, default=1,
    #                                              help_text='Código da situação tributária quanto ao Icms nesta '
    #                                                        'operação fiscal')
    situacao_tributaria_icms = models.IntegerField(default=1)

    base_calc_icms = models.DecimalField("Base de cálculo do ICMS", max_length=16, max_digits=16, decimal_places=2,
                                         default=0.00, help_text='Base de cálculo do ICMS.')
    perc_icms = models.DecimalField("Percentual do ICMS", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                    help_text='Percentual redução de base calc Icms.')
    perc_antec_tributaria = models.DecimalField("Percentual de antecipação tributária do ICMS", max_length=10,
                                                max_digits=10, decimal_places=6, default=0.00,
                                                help_text='Percentual de antecipação tributária do ICMS para efeito '
                                                          'de cálculo do custo de entrada')
    perc_red_icms = models.DecimalField("Percentual do ICMS", max_length=10, max_digits=10, decimal_places=6,
                                        default=0.00, help_text='Percentual redução de base calc Icms.')

    # 3 valor da operação/0 Margem Valor Agregado(%)/1 Pauta (Valor)/2 Preço Tabelado Máx.(vlr)
    modalidade_calculo_subst = models.CharField("Modalidade de cálculo da base Icms substituído?", max_length=1,
                                                null=False, default="3",
                                                help_text='Modalidade de cálculo da base Icms substituído')
    base_calc_icms_sub = models.DecimalField("Base de cálculo do Icms Substituição", max_length=16,
                                             max_digits=16, decimal_places=2, default=0.00)
    perc_mva_sub = models.DecimalField("Percentual do MVA", max_length=10, max_digits=10, decimal_places=6,
                                       default=0.00, help_text='MVA para efeito de cálculo da base de icms '
                                                               'substituição tributária')
    perc_icms_sub = models.DecimalField("Percentual do ICMS", max_length=10, max_digits=10, decimal_places=6,
                                        default=0.00, help_text='Percentual redução de base cálculo Icms.')
    perc_reducao_icms_sub = models.DecimalField("Percentual de reducao do ICMS Sub", max_length=10, max_digits=10,
                                                decimal_places=6, default=0.00,
                                                help_text='Percentual redução de base calc Icms substituição '
                                                          'tributária')

    base_calc_antecipacao_trib = models.DecimalField("Base de cálculo da antecipação tributária se houver.",
                                                     max_length=16, max_digits=16, decimal_places=2, default=0.00,
                                                     help_text='Base de cálculo da antecipação tributária se houver.')
    perc_antecipacao_trib = models.DecimalField("% para cálculo da antecipação tributária se houver.", max_length=10,
                                                max_digits=10, decimal_places=6, default=0.00,
                                                help_text='% para cálculo da antecipação tributária se houver.')

    # TODO Resolver depois
    # situacao_tributaria_pis = models.ForeignKey(SituacaoTribPis, on_delete=models.CASCADE, default=1,
    #                                             null=False, help_text='Código da situação tributária quanto ao pis '
    #                                                                   'nesta operação fiscal')
    situacao_tributaria_pis = models.IntegerField(default=1)

    base_calc_pis = models.DecimalField("Valor Base de cálculo do Pis", max_length=16, max_digits=16, decimal_places=2,
                                        default=0.00, help_text='Valor Base de cálculo do Pis')
    perc_pis = models.DecimalField("Percentual de redução de base do IPI", max_length=10, max_digits=10,
                                   decimal_places=6, default=0.00, help_text='Percentual de redução de base do IPI.')

    # Código da Base de Cálculo do Crédito apurado no período, conforme a Tabela 4.3.7. SPED PIS COFINS
    # TODO FALTA CRIAR A CLASSE NaturezaBasePis
    # natureza_base_pis = models.ForeignKey(NaturezaBasePis, on_delete=models.CASCADE, null=True, blank=True)
    # tabela 4.3.6 - Tabela Código de Tipo de Crédito - Atualizada em 03/01/2012 : REGISTRO M500: CRÉDITO DE COFINS
    # RELATIVO AO PERÍODO
    # TODO tipo_credito_base_pis = models.ForeignKey(CódigoTipoCreditoPis, on_delete=models.CASCADE)

    # TODO Resolver depois
    # situacao_tributaria_cofins = models.ForeignKey(SituacaoTribCofins, on_delete=models.CASCADE, default=1,
    #                                                help_text='Código da situação tributária quanto ao Cofins nesta '
    #                                                          'operação fiscal')
    situacao_tributaria_cofins = models.IntegerField(default=1)

    base_calc_cofins = models.DecimalField("Valor Base de cálculo do cofins", max_length=16, max_digits=16,
                                           decimal_places=2, default=0.00, help_text='Valor Base de cálculo do cofins')

    perc_fundo_pobreza = models.DecimalField("Percentual para fundo de combate a pobreza", max_length=10, max_digits=10,
                                             decimal_places=6, default=0.00, help_text='Percentual para fundo de '
                                                                                       'combate a pobreza')
    # LEI DA TAANSPARÊNCIA FISCAL NOTA TÉCNICA 003 2013 % DE TRIBUTOS TOTAL NESTE ITEM
    perc_trib_aproximado = models.DecimalField("Percentual", max_length=10, max_digits=10,
                                               decimal_places=6, default=0.00,
                                               help_text='Percentual aproximado de tributação conforme lei '
                                                         'transparência fiscal')

    base_calc_import = models.DecimalField("Valor Base de cálculo do imposto sobre importação", max_length=16,
                                           max_digits=16, decimal_places=2, default=0.00,
                                           help_text='Valor Base de cálculo do imposto sobre importação')
    perc_import = models.DecimalField("Percentual de II imposto sobre importação", max_length=10, max_digits=10,
                                      decimal_places=6, default=0.00,
                                      help_text='Percentual de II imposto sobre importação')

    # valor dos serviços se nfe for de serviços
    base_calc_issqn = models.DecimalField("Base de cálculo serviços", max_length=16, max_digits=16, decimal_places=2,
                                          default=0.00, help_text='valor Base de cálculo serviços se nfe for '
                                                                  'de serviços')
    perc_issqn = models.DecimalField("Percentual do ISS", max_length=10, max_digits=10, decimal_places=6, default=0.00,
                                     help_text='Percentual do ISS a recolher.')

    # % das despesas acessórias para rateio por item
    perc_desp_acessorias = models.DecimalField("Percentual de redução de base do IPI", max_length=10, max_digits=10,
                                               decimal_places=6, default=0.00, help_text='Percentual de redução de '
                                                                                         'base do IPI.')
    perc_seguro = models.DecimalField("Percentual de seguro neste Produto", max_length=10, max_digits=10,
                                      decimal_places=6, default=0.00, help_text='Percentual de seguro ')
    perc_frete = models.DecimalField("Percentual de frete neste Produto", max_length=10, max_digits=10,
                                     decimal_places=6, default=0.00, help_text='Percentual de frete ')

    # Natureza de custos deste tipo de operação de venda ou para qual conta de custos sistema irá
    # natureza_custos = models.ForeignKey(NaturezaCusto, default=1,
    #                                     on_delete=models.CASCADE,
    #                                     help_text='Natureza de custos deste tipo de operação de venda ou para qual '
    #                                               'conta de custos sistema irá')

    natureza_custos = models.PositiveIntegerField(default=1)

    # Centro de custos deste tipo de operação de venda ou para qual conta de custos sistema irá
    # centro_custo = models.ForeignKey(CentroCusto, default=1, on_delete=models.CASCADE,
    #                                  help_text='Centro de custos deste tipo de operação de venda ou para qual conta '
    #                                            'de custos sistema irá')

    centro_custo = models.PositiveIntegerField(default=1)

    # Código da promoção no cadastro de produtos corrente quando foi feita esta venda
    # codigo_promocao = models.ForeignKey(ProdutoPromocao, default=1, on_delete=models.CASCADE,
    #                                    help_text='Código da promoção desta venda na hora da venda')
    # TODO Resolver se vai ser obrigatório ou nao o preenchimento desse campo
    codigo_promocao = models.IntegerField(null=True, blank=True, default=0)
    ultima_alteracao = models.DateTimeField(null=True, blank=True)

    @staticmethod
    def get_absolute_url():
        return reverse('pedidos:pedido_list')

    def __str__(self):
        return 'Pedido: ' + str(self.pedido) + ' Produto: ' + str(self.produto)

    def tot_preco_unitario(self):
        return self.preco_unitario

    def total_preco_bruto(self):
        return self.preco_unitario * self.quantidade

    def valor_desconto(self):
        return (self.preco_unitario * self.quantidade) * (self.perc_desc / 100)

    def preco_liquido(self):
        valor = self.total_preco_bruto()
        valor -= self.valor_desconto()
        return valor

    class Meta:
        ordering = ['-pedido', 'sequencia']
        unique_together = ("pedido", "produto")
        verbose_name = 'Pedido Item'
        verbose_name_plural = 'Pedidos Itens'
