# Generated by Django 3.0.7 on 2020-06-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
