from django.db import models
from django.db.models.fields import BooleanField, FloatField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=10)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=20)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    dt_nasc = models.DateField
    dt_cadastro = models.DateField


class Livro(models.Model):
# usuario = Cliente
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    dt_cadastroLivro = models.DateField
    foto = models.ImageField
    ano_pub = models.IntegerField
    adicionar = models.CharField(max_length=50)
    vendido = models.BooleanField
    valor = models.FloatField
# categoria = Categoria 


class Venda (models.Model):
    data_venda = models.DateField
    cliente = models.CharField(max_length=50)
    valor = FloatField

class Categoria (models.Model):
    nome = models.CharField(max_length=50)

class FormaDePagamento (models.Model):
     descricao = models.CharField(max_length=50)



