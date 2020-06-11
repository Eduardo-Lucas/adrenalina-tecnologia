from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.empresas.models import Empresa
from apps.funcionarios.models import Funcionario


class FuncionarioListView(LoginRequiredMixin, ListView):
    model = Funcionario
    fields = ['all', ]
    context_object_name = 'funcionarios'
    template_name = 'funcionarios/funcionario_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioDetailView(LoginRequiredMixin, DetailView):
    pass


class FuncionarioCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = ['nome', 'telefone', 'email', 'ativo']

    success_message = 'O Funcionario %(nome)s foi criado com sucesso.'

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    context_object_name = 'funcionario'
    fields = ['nome', 'telefone', 'email', 'ativo']
    success_message = 'O Funcionario %(nome)s foi atualizado com sucesso.'


class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    pass
