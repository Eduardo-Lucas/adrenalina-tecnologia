# Generated by Django 3.0.7 on 2020-06-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20200613_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Empresa',
            new_name='empresa',
        ),
    ]
