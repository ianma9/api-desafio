# Generated by Django 3.1 on 2020-08-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
