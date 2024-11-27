from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.produtos, name='produtos'),
    path('produtos/<produto_id>/', views.produto, name='produto'),
    path('novo_produto', views.novo_produto, name='novo_produto'),
    path('editar_produto/<produto_id>', views.editar_produto, name='editar_produto'),
    path('excluir_produto/<produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('adicionar_ao_carrinho/<produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('excluir_produto_carrinho/<produto_id>/', views.excluir_produto_carrinho, name='excluir_produto_carrinho'),
]