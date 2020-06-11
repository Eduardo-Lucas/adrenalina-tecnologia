from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.core.choices import SIM_NAO_CHOICES
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    """Manutenção do Cadastro de Funcionários"""
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ativo = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='Sim')

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('funcionarios:funcionario_list')
