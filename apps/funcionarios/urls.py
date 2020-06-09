from django.urls import path

from apps.funcionarios.views import *
app_name = 'funcionarios'
urlpatterns = [
    path('list/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('create/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('update/<pk>', FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('delete/<pk>', FuncionarioDeleteView.as_view(), name='funcionario_delete'),

]
