# Generated by Django 3.0.7 on 2020-06-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='ativo',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Sim', max_length=3),
        ),
    ]
