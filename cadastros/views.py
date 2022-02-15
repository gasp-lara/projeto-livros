from msilib.schema import ListView
from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cliente, Livro, Venda, Categoria, FormaDePagamento
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nome", "email", "senha", "cep", "endereco", "numero", "bairro", "cidade", "estado", "dt_nasc", "dt_cadastro"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    
class LivroCreate(CreateView):
    model = Livro
    fields = ["usuario", "titulo", "autor", "editora", "descricao", "dt_cadastro", "foto", "ano_pub", "adicionar", "vendido", "valor", "categoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class VendaCreate(CreateView):
    model = Venda
    fields = ["dt_venda", "cliente", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class FormaDePagamentoCreate(CreateView):
    model = FormaDePagamento
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    ##update

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nome", "email", "senha", "cep", "endereco", "numero", "bairro", "cidade", "estado", "dt_nasc", "dt_cadastro"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    
class LivroUpdate(UpdateView):
    model = Livro
    fields = ["usuario", "titulo", "autor", "editora", "descricao", "dt_cadastro", "foto", "ano_pub", "adicionar", "vendido", "valor", "categoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class VendaUpdate(UpdateView):
    model = Venda
    fields = ["dt_venda", "cliente", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class FormaDePagamentoUpdate(UpdateView):
    model = FormaDePagamento
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

##Delete

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

    
class LivroDelete(DeleteView):
    model = Livro
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")


class VendaDelete(DeleteView):
    model = Venda
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")


class FormaDePagamentoDelete(DeleteView):
    model = FormaDePagamento
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

##Listar

class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/listas/cliente.html"

class LivroList(ListView):
    model = Livro
    template_name = "cadastros/listas/livro.html"

class VendaList(ListView):
    model = Venda
    template_name = "cadastros/listas/venda.html"

class CategoriaList(ListView):
    model = Categoria
    template_name = "cadastros/listas/categoria.html"

class FormaDePagamentoList(ListView):
    model = FormaDePagamento
    template_name = "cadastros/listas/formaDePagamento.html"