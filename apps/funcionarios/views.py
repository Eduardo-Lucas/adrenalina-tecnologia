from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.funcionarios.models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    fields = ['all', ]
    context_object_name = 'funcionarios'
    template_name = 'funcionarios/funcionario_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioDetailView(DetailView):
    pass


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ('nome', )
    success_message = 'O Funcionario %(nome)s foi criado com sucesso.'

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'
    success_message = 'O Funcionario %(nome)s foi atualizado com sucesso.'


class FuncionarioDeleteView(DeleteView):
    pass