from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.core.choices import SIM_NAO_CHOICES, TIPO_PARTICIPANTE_CHOICES, FISICA_JURIDICA_CHOICES
from apps.empresas.models import Empresa
from apps.funcionarios.models import Funcionario


class Cliente(models.Model):
    """
    Esse cadastro pode ser um cliente, fornecedor, ambos ou uma transportadora
    """
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # tabelapreco = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE)
    razao_social = models.CharField(max_length=50, blank=False)
    ativo = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='Sim')
    tipo_participante = models.CharField(max_length=20, choices=TIPO_PARTICIPANTE_CHOICES, default='cliente')
    nome_fantasia = models.CharField("Nome Fantasia", max_length=50, blank=False)
    fisica_juridica = models.CharField("Tipo de Cliente", max_length=8, blank=False,
                                       choices=FISICA_JURIDICA_CHOICES, default='Juridica')
    cnpj_cpf = models.CharField("CNPJ/CPF", max_length=18, blank=True, null=True)
    inscricao_estadual = models.CharField("Inscricao Estadual", max_length=15, blank=False,
                                          default="ISENTO")
    inscricao_municipal = models.CharField("Inscrição Municipal", max_length=15,
                                           blank=True, default="ISENTO")

    # TODO Depois excluir a opção null=True
    codigo = models.CharField("Código", max_length=14, blank=True, null=True)

    vendedor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name="responsavel")

    # TODO 1. Depois excluir a opção null=True
    # regiao_de_venda = models.ForeignKey(RegiaoDeVenda, on_delete=models.CASCADE, blank=True, null=True)
    # regiao_de_venda = models.IntegerField(blank=True, null=True)

    # TODO 2. Depois excluir a opção null=True
    # grupo = models.ForeignKey(GrupoParticipante, on_delete=models.CASCADE, blank=True, null=True)

    endereco = models.CharField("Endereço", max_length=60, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=60, blank=True, null=True)
    numero = models.CharField("Número", max_length=20, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=50, blank=True, null=True)

    # TODO 3. Depois excluir a opção null=True
    # cidade = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)

    cep = models.CharField("CEP", max_length=9, null=True, blank=True, )

    # todo Criar a classe e Depois excluir a opção null=True
    # estado = models.ForeignKey(Uf, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField("UF", max_length=2, blank=True, null=True)

    # todo Depois excluir a opção null=True
    # pais = models.ForeignKey(PaisIbge, on_delete=models.CASCADE, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True, default='Brasil')

    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    celular = models.CharField("Celular", max_length=20, blank=True, null=True)

    email = models.CharField("E-mail", max_length=100, blank=True, null=True)

    ultima_alteracao = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_absolute_url():
        return reverse('clientes:cliente_list')

    def __str__(self):
        return str(self.razao_social)

    def exibe_complemento(self):
        if self.complemento:
            return self.complemento
        else:
            return "-"

    def exibe_bairro(self):
        if self.bairro:
            return self.bairro
        else:
            return "-"

    def exibe_email(self):
        if self.email:
            return self.email
        else:
            return "Favor atualizar E-mail."

    def exibe_fisica_juridica(self):
        if self.fisica_juridica == 'J':
            return "Pessoa Jurídica"
        else:
            return "Pessoa Física"

    class Meta:
        ordering = ['razao_social']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
