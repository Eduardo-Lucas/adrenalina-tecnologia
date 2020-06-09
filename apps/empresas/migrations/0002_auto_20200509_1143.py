# Generated by Django 3.0.6 on 2020-05-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='tipo_participante',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_fundacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='indicador_inscricao_estadual',
            field=models.CharField(choices=[('Não contribuinte', 'Não contribuinte'), ('Contribuinte', 'Contribuinte'), ('Contribuinte isento', 'Contribuinte isento')], default='Não contribuinte', max_length=20),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_SUFRAMA',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_estadual',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_municipal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='optante_simples',
            field=models.BooleanField(default=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone_celular',
            field=models.CharField(default='(071) 9 9999-9999', max_length=20),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone_comercial',
            field=models.CharField(default='(071) 9 9999-9999', max_length=20),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipo',
            field=models.CharField(choices=[('Física', 'Fisica'), ('Jurídica', 'Juridica')], default='Jurídica', max_length=10),
        ),
    ]