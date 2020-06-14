from django.shortcuts import render
from django.views.generic import ListView

from apps.financeiro.models import TipoPagamento, PrazoPagamento


class TipoPagamentoListView(ListView):
    model = TipoPagamento
    fields = '__all__'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return TipoPagamento.objects.filter(empresa=empresa_logada)


class PrazoPagamentoListView(ListView):
    model = PrazoPagamento
    fields = '__all__'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return PrazoPagamento.objects.filter(empresa=empresa_logada)
