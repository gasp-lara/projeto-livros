from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cliente, Livro, Venda, Categoria, FormaDePagamento
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nome", "email", "senha", "cep", "endereco", "numero", "bairro", "cidade", "estado", "dt_nasc", "dt_cadastro"]
    template_name = "cadastros/cadastros.html"
    success_url = reverse_lazy("")

    
class LivroCreate(CreateView):
    model = Livro
    fields = ["usuario", "titulo", "autor", "editora", "descricao", "dt_cadastro", "foto", "ano_pub", "adicionar", "vendido", "valor", "categoria"]
    template_name = "cadastros/cadastros.html"
    success_url = reverse_lazy("")


class VendaCreate(CreateView):
    model = Venda
    fields = ["dt_venda", "cliente", "valor"]
    template_name = "cadastros/cadastros.html"
    success_url = reverse_lazy("")


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/cadastros.html"
    success_url = reverse_lazy("")


class FormaDePagamentoCreate(CreateView):
    model = FormaDePagamento
    fields = ["nome"]
    template_name = "cadastros/cadastros.html"
    success_url = reverse_lazy("")
