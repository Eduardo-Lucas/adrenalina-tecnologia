from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.empresas.form import EmpresaForm
from apps.empresas.models import Empresa

# todo Colocar LoginRequiredMixin nas Generic Views


class EmpresaListView(ListView):
    model = Empresa
    fields = ['all', ]
    context_object_name = 'empresas'
    template_name = 'empresas/empresa_list.html'


class EmpresaDetailView(DetailView):
    pass


class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    success_message = 'A Empresa %(nome)s foi criada com sucesso.'

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    success_message = 'A Empresa %(nome)s foi atualizada com sucesso.'


class EmpresaDeleteView(DeleteView):
    pass


def painel_empresa(request):
    return render(request, 'empresas/empresa_painel.html', {})
