from endereco.models import Endereco
from rest_framework.serializers import ModelSerializer


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            "id",
            "logradouro",
            "bairro",
            "cidade",
            "estado",
            "numero",
            "principal"
        ]

