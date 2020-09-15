from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):

    list_display = ["nome", "sobrenome", "cpf", "telefone", "email"]


admin.site.register(Cliente, ClienteAdmin)

