# Generated by Django 3.0.7 on 2020-06-10 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]