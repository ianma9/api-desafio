# coding: utf-8

from django.db import models
from endereco.models import Endereco


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    foto = models.FileField(upload_to='clientes/images', blank=True)

    enderecos = models.ManyToManyField(Endereco)

    def __str(self):
        return self.pk

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome + self.sobrenome

