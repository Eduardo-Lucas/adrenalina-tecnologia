from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.empresas.models import Empresa


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
    fields = '__all__'
    success_message = 'A Empresa %(nome)s foi criada com sucesso.'

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()


class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = '__all__'
    success_message = 'A Empresa %(nome)s foi atualizada com sucesso.'


class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    pass


@login_required
def painel_empresa(request):
    empresa = Empresa.objects.get(id=request.user.funcionario.empresa.id)
    context = {
        'empresa': empresa,
    }
    return render(request, 'empresas/empresa_painel.html', context)
