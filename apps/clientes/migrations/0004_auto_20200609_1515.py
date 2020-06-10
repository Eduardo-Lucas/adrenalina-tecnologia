# Generated by Django 3.0.7 on 2020-06-09 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('clientes', '0003_auto_20200609_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel', to='funcionarios.Funcionario'),
        ),
    ]
