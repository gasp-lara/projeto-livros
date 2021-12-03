from django.db import models

# Create your models here.

class Categoria (models.Model):
    nome = models.CharField(max_length=50)

    def _str_(self): 
        return self.nome

class FormaDePagamento (models.Model):
     descricao = models.CharField(max_length=50)

     def _str_(self): 
        return self.descricao


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
    dt_nasc = models.DateField()
    dt_cadastro = models.DateField()

    def _str_(self):
        return self.nome + ' - ' + str(self.email)


class Livro(models.Model):
# usuario = Cliente
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    dt_cadastroLivro = models.DateField()
    foto = models.ImageField()
    ano_pub = models.IntegerField()
    adicionar = models.CharField(max_length=50)
    vendido = models.BooleanField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def _str_(self):
        return self.titulo + ' - ' + str(self.autor)

class Venda (models.Model):
    data_venda = models.DateField()
    cliente = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def _str_(self): 
        return self.data_venda + ' - ' + str(self.cliente) + ' - ' + str(self.valor)




