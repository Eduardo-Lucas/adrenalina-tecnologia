from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.caixas.forms import CaixaMovimentoFormSet
from apps.caixas.models import Caixa


class CaixaListView(LoginRequiredMixin, ListView):
    model = Caixa


class CaixaCreateView(LoginRequiredMixin, CreateView):
    model = Caixa
    fields = ['data_movimento', 'valor_inicial']

    def form_valid(self, form):
        caixa = form.save(commit=False)
        caixa.user = self.request.user
        caixa.save()
        return super(CaixaCreateView, self).form_valid(form)


class CaixaUpdateView(LoginRequiredMixin, UpdateView):
    model = Caixa
    fields = ['data_movimento', 'valor_inicial']
    success_message = "O pedido foi atualizado com sucesso!"
    success_url = reverse_lazy('caixas:caixa_list')

    def get_context_data(self, **kwargs):
        data = super(CaixaUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['caixa_movimentos'] = CaixaMovimentoFormSet(self.request.POST, instance=self.object)
        else:
            data['caixa_movimentos'] = CaixaMovimentoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        caixa_movimentos = context['caixa_movimentos']
        with transaction.atomic():
            self.object = form.save()

            if caixa_movimentos.is_valid():
                caixa_movimentos.save()

        return super(CaixaUpdateView, self).form_valid(form)


class CaixaDetailView(LoginRequiredMixin, DetailView):
    model = Caixa
    fields = '__all__'


class CaixaDeleteView(LoginRequiredMixin, DeleteView):
    model = Caixa
    fields = '__all__'
