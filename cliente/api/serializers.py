from cliente.models import Cliente
from endereco.api.serializers import EnderecoSerializer
from rest_framework.serializers import ModelSerializer


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "sobrenome", "cpf", "rg", "telefone", "email", "foto"]

