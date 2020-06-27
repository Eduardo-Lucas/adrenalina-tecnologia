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
    fields = ['nome', 'telefone', 'email', 'ativo', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade',
              'estado', 'pais', 'quantidade_clientes']

    success_message = 'O Funcionario %(nome)s foi criado com sucesso.'

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0]
        verifica_username = User.objects.get(username=username)
        if verifica_username:
            print('nome de usuario ja existe')
        else:
            funcionario.empresa = self.request.user.funcionario.empresa
            funcionario.user = User.objects.create(username=username)
            funcionario.cadastrado_por = self.request.user
            funcionario.save()
            return super(FuncionarioCreateView, self).form_valid(form)


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    context_object_name = 'funcionario'
    model = Funcionario
    fields = ['nome', 'telefone', 'email', 'ativo', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade',
              'estado', 'pais', 'quantidade_clientes']
    success_message = 'O Funcionario %(nome)s foi atualizado com sucesso.'


class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    pass
