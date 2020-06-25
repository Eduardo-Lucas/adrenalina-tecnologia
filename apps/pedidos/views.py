from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import View

from apps.clientes.models import Cliente
from apps.pedidos.forms import PedidoForm, PedidoItemFormSet
from apps.pedidos.models import Pedido, PedidoItem
from apps.produtos.models import Produto
from utils import render_to_pdf


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

    def get_context_data(self, **kwargs):
        data = super(PedidoCreateView, self).get_context_data(**kwargs)
        print(data)
        return data

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
                instances = pedido_items.save(commit=False)
                for instance in instances:
                    produto = Produto.objects.get(id=instance.produto.id)
                    instance.preco_unitario = produto.preco
                    instance.total_produto = instance.quantidade * instance.preco_unitario
                pedido_items.save()

        return super(PedidoUpdateView, self).form_valid(form)


def pedidoPDF(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    items = PedidoItem.objects.filter(pedido=pedido)
    template = get_template('pedidos/pedido.html')

    context = {
        "pedido": pedido,
        "items": items,

    }
    html = template.render(context)
    pdf = render_to_pdf('pedidos/pedido.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Pedido_%s.pdf" %(str(id))
        content = "inline; filename='%s'" % filename
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % filename
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
