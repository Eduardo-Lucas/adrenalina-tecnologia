# Generated by Django 3.0.7 on 2020-06-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_empresa_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='ativo',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Sim', max_length=3),
        ),
    ]
