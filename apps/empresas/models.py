from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.core.choices import INDICADOR_INSC_ESTADUAL_CHOICES, FISICA_JURIDICA_CHOICES, SIM_NAO_CHOICES


# todo Para aparecer a lista de Mesas, precisa indicar que serve refeiçoes
class Empresa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    serve_refeicao = models.BooleanField(default=False)
    # logotipo = models.ImageField(upload_to='empresas', null=True, blank=True)
    tipo = models.CharField(max_length=10, default='Jurídica', choices=FISICA_JURIDICA_CHOICES)
    ativo = models.BooleanField(default=True)
    razao_para_inativar = models.CharField(max_length=500, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True, )
    rg = models.CharField(max_length=11, blank=True, null=True, unique=True, )
    indicador_inscricao_estadual = models.CharField(max_length=20,
                                                    default='Não contribuinte',
                                                    choices=INDICADOR_INSC_ESTADUAL_CHOICES)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True)
    inscricao_municipal = models.CharField(max_length=20, null=True, blank=True)
    inscricao_SUFRAMA = models.CharField(max_length=20, null=True, blank=True)
    optante_simples = models.BooleanField(max_length=1, default=False)
    email = models.EmailField(help_text='Informe apenas um e-mail')
    telefone_comercial = models.CharField(max_length=20, default='(071) 9 9999-9999', )
    telefone_celular = models.CharField(max_length=20, default='(071) 9 9999-9999', )
    data_fundacao = models.DateField(null=True, blank=True)

    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)

    observacao = models.TextField('Observações', max_length=200, null=True, blank=True)

    # Contatos da Empresa
    # todo Depois criar uma Classe para armazenar mais de um Contato
    nome_contato = models.CharField(max_length=50, null=True, blank=True)
    email_contato = models.CharField(max_length=20, null=True, blank=True)
    telefone_contato = models.CharField(max_length=20, null=True, blank=True)
    cargo_contato = models.CharField(max_length=20, null=True, blank=True)

    cep = models.CharField(max_length=8, default=41000-000, )
    endereco = models.CharField(max_length=50, default='Rua do Sobe e Desce',)
    numero = models.CharField(max_length=10, default='s/n', )
    complemento = models.CharField(max_length=10, blank=True, null=True,)
    bairro = models.CharField(max_length=20, blank=True, null=True, )
    cidade = models.CharField(max_length=20, default='Salvador', )

    uf = models.CharField(max_length=2, default='SC', )
    pais = models.CharField(max_length=15, default='Brasil', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def is_ativo(self):
        if self.ativo:
            return 'Ativo'
        else:
            return 'Inativo'

    class Meta:
        ordering: ['nome']
        unique_together = ['nome', 'codigo']

    @staticmethod
    def get_absolute_url():
        return reverse('empresas:painel_empresa')
