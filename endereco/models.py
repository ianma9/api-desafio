# coding: utf-8

from django.db import models

class Endereco(models.Model):

    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    numero = models.IntegerField()

    principal = models.BooleanField(default=False)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.logradouro, self.bairro, self.numero)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

