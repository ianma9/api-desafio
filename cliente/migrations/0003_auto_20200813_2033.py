# Generated by Django 3.1 on 2020-08-13 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('cliente', '0002_cliente_enderecos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='cliente',
            name='enderecos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]