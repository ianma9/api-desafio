# Generated by Django 3.1 on 2020-08-20 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20200813_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='enderecos',
        ),
    ]
