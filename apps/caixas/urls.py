from django.urls import path

from .views import *
app_name = 'caixas'

urlpatterns = [
    path('list', CaixaListView.as_view(), name='caixa_list'),
    path('create', CaixaCreateView.as_view(), name='caixa_create'),
    path('update/<int:pk>', CaixaUpdateView.as_view(), name='caixa_update'),
    path('delete/<int:pk>', CaixaDeleteView.as_view(), name='caixa_delete'),
    path('detail/<int:pk>', CaixaDetailView.as_view(), name='caixa_detail'),

]
