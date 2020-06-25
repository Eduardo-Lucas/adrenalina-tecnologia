from django import forms

from apps.empresas.models import Empresa


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = '__all__'
        labels = {
            'nome': 'Nome da Empresa',
            'razao_social': 'Razão Social',
            'tipo': 'Tipo',
            'ativo': 'Status da Empresa',
            'serve_refeicao': 'Serve Refeição',
            'codigo': 'Código da Empresa',
            'cnpj': 'CNPJ',
            'cpf': 'CPF',
            'rg': 'RG',
            'indicador_inscricao_estadual': 'Indicador de inscrição estadual',
            'inscricao_estadual': 'Inscrição estadual',
            'inscricao_municipal': 'Inscrição municipal',
            'inscricao_SUFRAMA': 'Inscrição SUFRAMA',
            'optante_simples': 'Optante pelo SIMPLES',
            'telefone_comercial': 'Telefone Comercial',
            'telefone_celular': 'Telefone Celular',
            'observacao': 'Observações',
            'email': 'Email Principal',
            'data_fundacao': 'Data de Fundação (DD/MM/AAAA)',
            'codigo': 'Código do Participante',
            'cep': 'CEP',
            'uf': 'Estado',
        }
