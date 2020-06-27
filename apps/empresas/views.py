from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.clientes.models import Cliente
from apps.empresas.forms import EmpresaForm
from apps.empresas.models import Empresa
from apps.funcionarios.models import Funcionario
from apps.pedidos.models import Pedido
from apps.produtos.models import Produto


class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    fields = ['all', ]
    context_object_name = 'empresas'
    template_name = 'empresas/empresa_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa.id
        return Empresa.objects.filter(id=empresa_logada)


class EmpresaDetailView(LoginRequiredMixin, DetailView):
    pass


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    form_class = EmpresaForm
    success_message = 'A Empresa %(nome)s foi criada com sucesso.'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.ativo = True
        obj.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect('empresas:painel_empresa')


class EmpresaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    success_message = 'A Empresa %(nome)s foi atualizada com sucesso.'
    success_url = reverse_lazy('empresas:painel_empresa')


class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    pass


@login_required
def painel_empresa(request):
    empresa = Empresa.objects.get(id=request.user.funcionario.empresa.id)
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa.id)
    clientes = Cliente.objects.filter(empresa=request.user.funcionario.empresa.id)
    produtos = Produto.objects.filter(empresa=request.user.funcionario.empresa.id)
    pedidos = Pedido.objects.filter(empresa=request.user.funcionario.empresa.id)

    context = {
        'empresa': empresa,
        'funcionarios': funcionarios,
        'clientes': clientes,
        'produtos': produtos,
        'pedidos': pedidos,
    }
    return render(request, 'empresas/empresa_painel.html', context)


def pagina_administrador(request):
    empresas = Empresa.objects.all()
    context = {
        'empresas': empresas,
    }
    return render(request, 'empresas/pagina_administrador.html', context)
