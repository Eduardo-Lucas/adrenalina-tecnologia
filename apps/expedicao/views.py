from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView

from apps.pedidos.models import Pedido, PedidoStatus


def expedicao(request):
    empresa = request.user.funcionario.empresa
    pedidos_separar = Pedido.objects.filter(Q(pedidostatus=2) | Q(pedidostatus=6), empresa=empresa)
    pedidos_em_separacao = Pedido.objects.filter(pedidostatus=11, empresa=empresa)
    pedidos_separados = Pedido.objects.filter(pedidostatus=12, empresa=empresa)

    return render(request, 'expedicao/expedicao.html',
                  {'pedidos_separar': pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados': pedidos_separados})


@require_POST
def inicia_separacao(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.pedidostatus = PedidoStatus.objects.get(id=11)
    pedido.save()

    pedidos_separar = Pedido.objects.filter(Q(pedidostatus=2) | Q(pedidostatus=6))
    pedidos_em_separacao = Pedido.objects.filter(pedidostatus=11)
    pedidos_separados = Pedido.objects.filter(pedidostatus=12)

    return render(request, 'expedicao/expedicao.html',
                  {'pedidos_separar': pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados': pedidos_separados})


@require_POST
def finaliza_separacao(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.pedidostatus = PedidoStatus.objects.get(id=12)
    pedido.save()

    pedidos_separar = Pedido.objects.filter(Q(pedidostatus=2) | Q(pedidostatus=6))
    pedidos_em_separacao = Pedido.objects.filter(pedidostatus=11)
    pedidos_separados = Pedido.objects.filter(pedidostatus=12)

    return render(request, 'expedicao/expedicao.html',
                  {'pedidos_separar': pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados': pedidos_separados})


@require_POST
def estorna_separacao(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.pedidostatus = PedidoStatus.objects.get(id=2)
    pedido.save()

    pedidos_separar = Pedido.objects.filter(Q(pedidostatus=2) | Q(pedidostatus=6))
    pedidos_em_separacao = Pedido.objects.filter(pedidostatus=11)
    pedidos_separados = Pedido.objects.filter(pedidostatus=12)

    return render(request, 'expedicao/expedicao.html',
                  {'pedidos_separar': pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados': pedidos_separados})


class AlteraLojaUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = ['loja', ]
    context_object_name = 'pedido'
    template_name = 'expedicao/altera_loja.html'
