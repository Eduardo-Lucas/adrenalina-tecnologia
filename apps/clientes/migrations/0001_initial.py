# Generated by Django 3.0.7 on 2020-06-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=50)),
                ('tipo_participante', models.CharField(choices=[('cliente', 'Cliente'), ('fornecedor', 'Fornecedor'), ('ambos', 'Ambos'), ('transportadora', 'Transportadora')], default='cliente', max_length=20)),
                ('nome_fantasia', models.CharField(max_length=50, verbose_name='Nome Fantasia')),
                ('fisica_juridica', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], default='J', max_length=1, verbose_name='Tipo de Cliente')),
                ('cnpj_cpf', models.CharField(blank=True, max_length=18, null=True, verbose_name='CNPJ/CPF')),
                ('inscricao_estadual', models.CharField(default='ISENTO', max_length=15, verbose_name='Inscricao Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, default='ISENTO', max_length=15, verbose_name='Inscrição Municipal')),
                ('codigo', models.CharField(blank=True, max_length=14, null=True, verbose_name='Código')),
                ('endereco', models.CharField(blank=True, max_length=60, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=60, null=True, verbose_name='Complemento')),
                ('numero', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='E-mail')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel', to='funcionarios.Funcionario')),
            ],
            options={
                'verbose_name': 'Cadastro de Cliente',
                'verbose_name_plural': 'Cadastro de Clientes',
                'ordering': ['razao_social'],
            },
        ),
    ]
