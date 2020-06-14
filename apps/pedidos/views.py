from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.pedidos.forms import PedidoForm, PedidoItemFormSet
from apps.pedidos.models import Pedido


class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    fields = '__all__'
    context_object_name = 'pedidos'
    template_name = 'pedidos/pedido_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Pedido.objects.filter(empresa=empresa_logada)


class PedidoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos:pedido_list')

    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido.empresa = self.request.user.funcionario.empresa
        pedido.vendedor = self.request.user
        pedido.save()
        return super(PedidoCreateView, self).form_valid(form)


class PedidoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_message = "O pedido foi atualizado com sucesso!"
    success_url = reverse_lazy('pedidos:pedido_list')

    def get_context_data(self, **kwargs):
        data = super(PedidoUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['pedido_items'] = PedidoItemFormSet(self.request.POST, instance=self.object)
        else:
            data['pedido_items'] = PedidoItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pedido_items = context['pedido_items']
        with transaction.atomic():
            self.object = form.save()

            if pedido_items.is_valid():
                pedido_items.save()

        return super(PedidoUpdateView, self).form_valid(form)
