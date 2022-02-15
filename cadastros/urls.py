from .views import name
from django.urls import path

from .views import ClienteCreate, LivroCreate, VendaCreate, CategoriaCreate, FormaDePagamentoCreate
from .views import ClienteUpdate, LivroUpdate, VendaUpdate, CategoriaUpdate, FormaDePagamentoUpdate
from .views import ClienteDelete, LivroDelete, VendaDelete, CategoriaDelete, FormaDePagamentoDelete
from .views import ClienteList, LivroList, VendaList, CategoriaList, FormaDePagamentoList

urlpatterns = [

    path('cadastrar/cliente', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/livro', LivroCreate.as_view(), name='cadastrar-livro'),  
    path('cadastrar/venda', VendaCreate.as_view(), name='cadastrar-venda'),
    path('cadastrar/categoria', CategoriaCreate.as_view(), name='cadastrar-categoria'),  
    path('cadastrar/formaDePagamento', FormaDePagamentoCreate.as_view(), name='cadastrar-formaDePagamento'),  

    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar-livro'),  
    path('editar/venda/<int:pk>/', VendaUpdate.as_view(), name='editar-venda'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),  
    path('editar/formaDePagamento/<int:pk>/', FormaDePagamentoUpdate.as_view(), name='editar-formaDePagamento'), 

    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),  
    path('excluir/venda/<int:pk>/', VendaDelete.as_view(), name='excluir-venda'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),  
    path('excluir/formaDePagamento/<int:pk>/', FormaDePagamentoDelete.as_view(), name='excluir-formaDePagamento'), 

    path('listar/clientes/', ClienteDelete.as_view(), name='listar-clientes'),
    path('listar/livros/', LivroDelete.as_view(), name='listar-livros'),  
    path('listar/vendas/', VendaDelete.as_view(), name='listar-vendas'),
    path('listar/categorias/', CategoriaDelete.as_view(), name='listar-categorias'),  
    path('lisrar/formasDePagamento/', FormaDePagamentoDelete.as_view(), name='listar-formasDePagamento'), 

]