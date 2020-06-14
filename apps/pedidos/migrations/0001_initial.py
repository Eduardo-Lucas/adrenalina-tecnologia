# Generated by Django 3.0.7 on 2020-06-14 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0004_auto_20200613_1225'),
        ('empresas', '0003_empresa_serve_refeicao'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financeiro', '0003_auto_20200613_1040'),
        ('lojas', '0002_auto_20200613_1040'),
        ('produtos', '0004_auto_20200612_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(default=1, unique=True)),
                ('aberta', models.BooleanField(default=True, help_text='A mesa tem que estar aberta para constar no Pedido')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
            ],
            options={
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='PedidoStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(default='MAT', max_length=3)),
                ('subserie', models.CharField(default='VEN', max_length=3)),
                ('indicador_pagamento_nfe', models.CharField(default='0', help_text='Indicador da forma de pagamento para informação na nota fiscal eletrônica', max_length=1, verbose_name='Indicador da forma de pagamento')),
                ('regime_tributario', models.CharField(default='1', help_text='código do regime tributário do emitente ou do fornecedor 1-Simples na 2-Simples exc  3-Normal', max_length=1, verbose_name='Regime Tributário Emitente')),
                ('autorizacao_faturamento', models.CharField(blank=True, help_text='Número da autorização de faturamento emitida pelo cliente ou pelo fornecedor', max_length=20, null=True, verbose_name='Número da autorização para Faturamento')),
                ('autorizacao_numitem', models.PositiveIntegerField(default=0, verbose_name='Número do Pedido')),
                ('indicador_emitente', models.CharField(default='1', help_text='Indicador de emitente do documento fiscal  0_Emissão própria 1_Terceiros', max_length=1, null=True, verbose_name='Indicador de emitente da NFe')),
                ('situacaodocumentosped', models.PositiveIntegerField(default=1)),
                ('modelodocumentofiscal', models.PositiveIntegerField(default=1)),
                ('data_pedido', models.DateField(auto_now_add=True, verbose_name='Data do Pedido')),
                ('data_emissao', models.DateField(auto_now_add=True, verbose_name='Data de De Emissão da Nfe')),
                ('data_saida', models.DateTimeField(auto_now_add=True, verbose_name='Data de saida para entrega')),
                ('data_movimento', models.DateTimeField(auto_now_add=True, verbose_name='Data de Movimentação da Nfe')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tipo_pedido', models.CharField(default='saida', max_length=10)),
                ('indicador_presenca_nfe', models.CharField(default='1', help_text='indPres (nfe 3.10) Indicador de presença do comprador no estabelecimento comercial no momento da operação', max_length=1, verbose_name='Indicador de presença do comprador NFe')),
                ('tipo_preco_pedido', models.CharField(default='V', help_text='Tipo de Preço usado na saida de pedidos V Preço VENDA / C Último CUSTO / I Preço indexado, etc', max_length=1)),
                ('total_produtos', models.DecimalField(decimal_places=2, default=0.0, help_text='Total bruto (sem descontos) dos  produtos no pedido', max_digits=16, max_length=16, verbose_name='Total dos Produtos')),
                ('perc_desc', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de descontos nos produtos', max_digits=10, max_length=10, verbose_name='Percentual de descontos nos produtos')),
                ('descont_valor', models.DecimalField(decimal_places=2, default=0.0, help_text='valor do desconto na nota fiscal em totais (valor dos descontos em % + valor dos descontos em valores do pedido', max_digits=16, max_length=16, verbose_name='Valor desconto no Pedido')),
                ('base_calc_ipi', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo do IPI', max_digits=16, max_length=16, verbose_name='Base de cálculo do IPI')),
                ('valor_ipi', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor calculado do IPI a recolher.', max_digits=16, max_length=16, verbose_name='Valor do IPI')),
                ('perc_ipi', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual do IPI a recolher.', max_digits=10, max_length=10, verbose_name='Percentual do IPI')),
                ('valor_contabil', models.DecimalField(decimal_places=2, default=0.0, help_text='Total líquido do pedido/total líquido da Nota fiscal pedido.', max_digits=16, max_length=16, verbose_name='Total líquido do Pedido')),
                ('base_calc_icms', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo do ICMS.', max_digits=16, max_length=16, verbose_name='Base de cálculo do ICMS')),
                ('valor_icms', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor calculado do ICMS a recolher.', max_digits=16, max_length=16, verbose_name='Valor do ICMS')),
                ('perc_icms', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual do ICMS a recolher.', max_digits=10, max_length=10, verbose_name='Percentual do ICMS')),
                ('base_calc_icms_sub', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo do Icms Substituição tributária', max_digits=16, max_length=16, verbose_name='Base de cálculo do Icms Substituição')),
                ('valor_icms_sub', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do ICMS substituição tributária', max_digits=16, max_length=16, verbose_name='Valor do ICMS substituição tributária')),
                ('valor_despesas_acess', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor das despesas acessorias', max_digits=16, max_length=16, verbose_name='Valor despesas acessorias')),
                ('base_calc_pis', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor Base de cálculo do Pis', max_digits=16, max_length=16, verbose_name='Valor Base de cálculo do Pis')),
                ('valor_pis', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do pis', max_digits=16, max_length=16, verbose_name='Valor do Pis')),
                ('base_calc_cofins', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor Base de cálculo do cofins', max_digits=16, max_length=16, verbose_name='Valor Base de cálculo do cofins')),
                ('valor_cofins', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do cofins', max_digits=16, max_length=16, verbose_name='Valor do cofins')),
                ('valor_seguro', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do cofins', max_digits=16, max_length=16, verbose_name='Valor do cofins')),
                ('base_calc_issqn', models.DecimalField(decimal_places=2, default=0.0, help_text='valor Base de cálculo serviços se nfe for de serviços', max_digits=16, max_length=16, verbose_name='Base de cálculo serviços')),
                ('perc_issqn', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual do ISS a recolher.', max_digits=10, max_length=10, verbose_name='Percentual do ISS')),
                ('quantidade_servicos', models.DecimalField(decimal_places=6, default=0.0, help_text='Quantidade dos serviços se nfe for de serviços', max_digits=10, max_length=10, verbose_name='Quantidade de serviços')),
                ('valor_servicos', models.DecimalField(decimal_places=2, default=0.0, help_text='valor dos serviços se nfe for de serviços', max_digits=16, max_length=16, verbose_name='Valor dos serviços')),
                ('valor_frete', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do frete na nota fiscal de entrada ou de saida', max_digits=16, max_length=16, verbose_name='Valor do FRETE')),
                ('valor_icm_frete', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor do icms sobre o frete na nota fiscal de entrada ou de saida', max_digits=16, max_length=16, verbose_name='Valor do icms sobre o frete')),
                ('cif_fob_frete', models.CharField(default='1', help_text='Indicador de frete. 0-Emitente, 1-Destinatário , 2-Terceiros, 3-Próprio remetente, 4-próprio destinatário, 9-Sem', max_length=1, verbose_name='Indicador do tipo de frete')),
                ('tipo_frete', models.CharField(default='1', help_text='1 Frete na NFe COM cre 2-Incluso na Nfe sem crédito 3-Conhec a parte 4-Conhec parte sem cred', max_length=1, verbose_name='Indicador do custo do frete')),
                ('status_manifestacao', models.CharField(default='C', help_text='Status de conferencia na manifestação de destinatário para efeito de liberação de produtos para venda', max_length=1)),
                ('status_contabilidade', models.CharField(default='C', help_text='Status de conferencia da NF  pela contabilidade informando que nf está fiscalmente OK', max_length=1)),
                ('status_financeiro', models.CharField(default='A', help_text='Status de conferencia da NF  pelo departamento financeiro informando que nf está financeiramente (contas a pagar) OK', max_length=1)),
                ('status_precos', models.CharField(default='C', help_text='Status de conferencia da NF  pelo departamento custos informando que nf está com preços e custos OK', max_length=1)),
                ('status_expedicao', models.CharField(default='L', help_text='Status de conferencia da NF  pela expedição informando que nf está com quantidades armazenadas OK', max_length=1)),
                ('status_diferenca', models.CharField(default='C', help_text='Status de conferencia dos valores na nota fiscal de entrada ou saida para ver se há diferenças ', max_length=1)),
                ('observacoes', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observações')),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('empresa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
                ('loja', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lojas.Loja')),
                ('mesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.Mesa')),
                ('pedidostatus', models.ForeignKey(default=2, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='pedidos.PedidoStatus')),
                ('prazo_de_pagamento', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='financeiro.PrazoPagamento')),
                ('tipo_de_pagamento', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tipopagamentoWeb', to='financeiro.TipoPagamento')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencia', models.PositiveIntegerField(default=1, verbose_name='Sequência do item')),
                ('unidade', models.CharField(default='UN', help_text='Unidade do produto vendido conforme cadastro no momento da venda. A mesma do cadastro de produtos', max_length=13)),
                ('descricao', models.CharField(default='Descricao', help_text='Descrição do produto vendido conforme cadastro no momento da venda. A mesma do cadastro de produtos', max_length=60)),
                ('observacoes', models.CharField(blank=True, default=' ', help_text='Observação para efeito de informação fiscal específica neste produto', max_length=40, null=True)),
                ('cfop', models.IntegerField(default=5102)),
                ('codigo_ncm', models.CharField(default=0, max_length=100)),
                ('codigo_cest', models.IntegerField(default=0)),
                ('status_pedido_item', models.CharField(default='N', help_text='status do pedido Orçamento / Devolução /Cancelado /Em análise crédito /Bloqueado/ Faturado / quitado etc ', max_length=1, verbose_name='Status deste pedido')),
                ('autorizacao_faturamento', models.CharField(blank=True, help_text='Número da autorização de faturamento emitida pelo cliente ou pelo fornecedor', max_length=20, null=True, verbose_name='Número da autorização para Faturamento')),
                ('autorizacao_numitem', models.PositiveIntegerField(default=0, verbose_name='Número do Pedido')),
                ('quantidade', models.DecimalField(decimal_places=0, default=1, max_digits=16, max_length=16, verbose_name='Quantidade')),
                ('peso_liquido', models.DecimalField(decimal_places=6, default=0.0, help_text='peso líquido deste produto', max_digits=16, max_length=16, verbose_name='Peso líquido do produto')),
                ('peso_bruto', models.DecimalField(decimal_places=6, default=0.0, help_text='peso bruto deste produto', max_digits=16, max_length=16, verbose_name='Peso bruto do produto')),
                ('metro_cubico', models.DecimalField(decimal_places=6, default=0.0, help_text='metros cúbicos do produto', max_digits=16, max_length=16, verbose_name='metros cúbicos do produto')),
                ('movimenta_estoques', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', help_text='S para movimentar estoques e N para nao movimentar', max_length=3, verbose_name='Movimenta Estoques?')),
                ('saldo_fisico', models.DecimalField(decimal_places=6, default=0.0, help_text='Saldo físico do produto após gravação', max_digits=16, max_length=16, verbose_name='Saldo físico do produto após gravação do pedido')),
                ('saldo_fiscal', models.DecimalField(decimal_places=6, default=0.0, help_text='Saldo fiscal do produto após geração e gravação da nota fiscal emitida ou recebida', max_digits=16, max_length=16, verbose_name='Saldo físico do produto após gravação')),
                ('preco_custo', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço de custo do produto após gravação da nota fiscal de entrada ou saida', max_digits=16, max_length=16, verbose_name='Preço de custo calculado após gravação')),
                ('preco_venda', models.DecimalField(decimal_places=2, default=0.0, help_text='Preço de Venda', max_digits=16, max_length=16, verbose_name='Preço de Venda')),
                ('preco_medio', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço de custo médio do produto após gravação da nota fiscal de entrada ou saida', max_digits=16, max_length=16, verbose_name='Preço de custo médio calculado após gravação')),
                ('preco_custo_nfe', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço de custo do produto após gravação da nota fiscal de entrada ou saida', max_digits=16, max_length=16, verbose_name='Preço de custo calculado após gravação da NFe')),
                ('preco_medio_nfe', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço de custo médio do produto após gravação a nota fiscal de entrada ou saida', max_digits=16, max_length=16, verbose_name='Preço de custo médio calculado após gravação da Nfe')),
                ('preco_unitario', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço unitário de venda conforme negociação e configurações do sistema', max_digits=16, max_length=16, verbose_name='Preço Unitário')),
                ('perc_desc', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de descontos nos produtos', max_digits=10, max_length=10, verbose_name='% Desc')),
                ('custo_informado', models.DecimalField(decimal_places=6, default=0.0, help_text='Preço gerencial de venda conforme negociação para efeito de cálculo de Preço de venda', max_digits=16, max_length=16, verbose_name='Preço gerencial de venda')),
                ('data_movimento', models.DateTimeField(auto_now_add=True, help_text='Data de Movimentação do produto. Mesma data do pedido para efeito de cálculo de saldos (Codigo+data)', verbose_name='Data de Movimentação do produto')),
                ('total_produto', models.DecimalField(decimal_places=2, default=0.0, help_text='Total bruto (sem descontos) do produto no pedido', max_digits=16, max_length=16, verbose_name='Total do Produto')),
                ('modalidade_ipi', models.CharField(default='1', help_text='Modalidade de cálculo da base Icms', max_length=1, verbose_name='Modalidade de cálculo do IPI ?')),
                ('situacao_tributaria_ipi', models.IntegerField(default=1)),
                ('base_calc_ipi', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo do IPI=valor produtos - descontos', max_digits=16, max_length=16, verbose_name='Base de cálculo do IPI')),
                ('perc_ipi', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual do IPI a recolher.', max_digits=10, max_length=10, verbose_name='Percentual do IPI')),
                ('perc_red_ipi', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de redução de base do IPI.', max_digits=10, max_length=10, verbose_name='Percentual de redução de base do IPI')),
                ('modalidade_calculo', models.CharField(default='3', help_text='Modalidade de cálculo da base Icms', max_length=1, verbose_name='Modalidade de cálculo da base Icms?')),
                ('modalidade_icms', models.CharField(default='3', help_text='Modalidade de cálculo da base Icms', max_length=1, verbose_name='Modalidade de cálculo da base Icms?')),
                ('situacao_tributaria_icms', models.IntegerField(default=1)),
                ('base_calc_icms', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo do ICMS.', max_digits=16, max_length=16, verbose_name='Base de cálculo do ICMS')),
                ('perc_icms', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual redução de base calc Icms.', max_digits=10, max_length=10, verbose_name='Percentual do ICMS')),
                ('perc_antec_tributaria', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de antecipação tributária do ICMS para efeito de cálculo do custo de entrada', max_digits=10, max_length=10, verbose_name='Percentual de antecipação tributária do ICMS')),
                ('perc_red_icms', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual redução de base calc Icms.', max_digits=10, max_length=10, verbose_name='Percentual do ICMS')),
                ('modalidade_calculo_subst', models.CharField(default='3', help_text='Modalidade de cálculo da base Icms substituído', max_length=1, verbose_name='Modalidade de cálculo da base Icms substituído?')),
                ('base_calc_icms_sub', models.DecimalField(decimal_places=2, default=0.0, max_digits=16, max_length=16, verbose_name='Base de cálculo do Icms Substituição')),
                ('perc_mva_sub', models.DecimalField(decimal_places=6, default=0.0, help_text='MVA para efeito de cálculo da base de icms substituição tributária', max_digits=10, max_length=10, verbose_name='Percentual do MVA')),
                ('perc_icms_sub', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual redução de base cálculo Icms.', max_digits=10, max_length=10, verbose_name='Percentual do ICMS')),
                ('perc_reducao_icms_sub', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual redução de base calc Icms substituição tributária', max_digits=10, max_length=10, verbose_name='Percentual de reducao do ICMS Sub')),
                ('base_calc_antecipacao_trib', models.DecimalField(decimal_places=2, default=0.0, help_text='Base de cálculo da antecipação tributária se houver.', max_digits=16, max_length=16, verbose_name='Base de cálculo da antecipação tributária se houver.')),
                ('perc_antecipacao_trib', models.DecimalField(decimal_places=6, default=0.0, help_text='% para cálculo da antecipação tributária se houver.', max_digits=10, max_length=10, verbose_name='% para cálculo da antecipação tributária se houver.')),
                ('situacao_tributaria_pis', models.IntegerField(default=1)),
                ('base_calc_pis', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor Base de cálculo do Pis', max_digits=16, max_length=16, verbose_name='Valor Base de cálculo do Pis')),
                ('perc_pis', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de redução de base do IPI.', max_digits=10, max_length=10, verbose_name='Percentual de redução de base do IPI')),
                ('situacao_tributaria_cofins', models.IntegerField(default=1)),
                ('base_calc_cofins', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor Base de cálculo do cofins', max_digits=16, max_length=16, verbose_name='Valor Base de cálculo do cofins')),
                ('perc_fundo_pobreza', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual para fundo de combate a pobreza', max_digits=10, max_length=10, verbose_name='Percentual para fundo de combate a pobreza')),
                ('perc_trib_aproximado', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual aproximado de tributação conforme lei transparência fiscal', max_digits=10, max_length=10, verbose_name='Percentual')),
                ('base_calc_import', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor Base de cálculo do imposto sobre importação', max_digits=16, max_length=16, verbose_name='Valor Base de cálculo do imposto sobre importação')),
                ('perc_import', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de II imposto sobre importação', max_digits=10, max_length=10, verbose_name='Percentual de II imposto sobre importação')),
                ('base_calc_issqn', models.DecimalField(decimal_places=2, default=0.0, help_text='valor Base de cálculo serviços se nfe for de serviços', max_digits=16, max_length=16, verbose_name='Base de cálculo serviços')),
                ('perc_issqn', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual do ISS a recolher.', max_digits=10, max_length=10, verbose_name='Percentual do ISS')),
                ('perc_desp_acessorias', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de redução de base do IPI.', max_digits=10, max_length=10, verbose_name='Percentual de redução de base do IPI')),
                ('perc_seguro', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de seguro ', max_digits=10, max_length=10, verbose_name='Percentual de seguro neste Produto')),
                ('perc_frete', models.DecimalField(decimal_places=6, default=0.0, help_text='Percentual de frete ', max_digits=10, max_length=10, verbose_name='Percentual de frete neste Produto')),
                ('natureza_custos', models.PositiveIntegerField(default=1)),
                ('centro_custo', models.PositiveIntegerField(default=1)),
                ('codigo_promocao', models.IntegerField(blank=True, default=0, null=True)),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pedidos.Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
            ],
            options={
                'verbose_name': 'Pedido Item',
                'verbose_name_plural': 'Pedidos Itens',
                'ordering': ['-pedido', 'sequencia'],
                'unique_together': {('pedido', 'produto')},
            },
        ),
    ]
