# Generated by Django 3.1 on 2020-08-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_endereco_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='cliente',
        ),
    ]