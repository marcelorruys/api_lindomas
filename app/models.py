from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=120)
    uf = models.CharField(max_length=60)
    cep = models.CharField(max_length=20)
    bairro = models.CharField(max_length=120)
