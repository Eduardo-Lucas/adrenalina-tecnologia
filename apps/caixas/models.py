from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.core.choices import STATUS_CAIXA_CHOICES
from apps.financeiro.models import TipoPagamento


class Caixa(models.Model):
    data_movimento = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=7, choices=STATUS_CAIXA_CHOICES, default='Aberto')
    valor_inicial = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    tipopagamento = models.ForeignKey(TipoPagamento, on_delete=models.PROTECT)
    valor_movimento = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        ordering = ['-data_movimento']

    def __str__(self):
        return str(self.data_movimento) + ' - ' + str(self.user) + ' - ' + self.status

    @staticmethod
    def get_absolute_url():
        return reverse('caixa:caixa_list')
