from django import forms

from apps.clientes.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'nome': 'Nome do Cliente',
            'razao_social': 'Razão Social',
            'tipo_participante': 'Tipo de Cliente',
            'nome_fantasia': 'Nome Fantasia',
            'fisica_juridica': 'Física/Jurídica',
            'cnpj_cpf': 'CNPJ/CPF',
            'inscricao_estadual': 'Inscrição Estadual',
            'inscricao_municipal': 'Inscrição Municipal',
            'codigo': 'Código do Cliente',
            'vendedor': 'Vendedor Responsável',
            'endereco': 'Endereço',
            'complemento': 'Complemento',
            'numero': 'Número',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'cep': 'CEP',
            'estado': 'Estado',
            'pais': 'País',
            'telefone': 'Telefone',
            'celular': 'Celular',
            'email': 'E-mail',
        }
