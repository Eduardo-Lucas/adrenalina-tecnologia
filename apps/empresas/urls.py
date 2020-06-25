from django.urls import path

from apps.empresas.views import *
app_name = 'empresas'
urlpatterns = [
    path('list/', EmpresaListView.as_view(), name='empresa_list'),
    path('create/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('update/<pk>', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('delete/<pk>', EmpresaDeleteView.as_view(), name='empresa_delete'),


    path('painel/', painel_empresa, name='painel_empresa'),
    path('pagina_administrador/', pagina_administrador, name='pagina_administrador'),

]
