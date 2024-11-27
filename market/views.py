from django.shortcuts import render
from .models import Produto, Carrinho, ItemCarrinho
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

def index(request):
    carrinho = Carrinho.objects.filter(usuario=request.user, ativo=True).first()  # Carrega o carrinho do usuário logado
    produtos = Produto.objects.all()  # Busca todos os produtos
    context = {'carrinho': carrinho, 'produtos': produtos}
    return render(request, 'market/index.html', context)

@login_required
def produtos(request):
    produtos = Produto.objects.all() 
    context = {'produtos': produtos}
    return render(request, 'market/produtos.html',context)

@login_required
def produto(request, produto_id):
    """Display a single topic and its entries"""
    produto = Produto.objects.get(id=produto_id) 

    # if produto.owner!=request.user:
    #     raise Http404("Você não tem permissão para acessar este produto.")
    context = {'produto': produto}
    return render(request, 'market/produto.html',context)

@login_required
def novo_produto(request):
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = ProdutoForm()
    else:
        # Dados de POST submetidos; processa os dados
        file = request.FILES.get('imagem')  # O nome do campo deve corresponder ao nome no form
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.imagem = file  # Associa o arquivo manualmente
            produto.save()
            print("Produto criado!")
            return HttpResponseRedirect(reverse('produtos'))
    context = {'form': form}
    return render(request, 'market/novo_produto.html', context)

@login_required
@superuser_required
def editar_produto(request, produto_id):
    """Edit an existing entry"""
    produto = Produto.objects.get(id=produto_id)

    if request.method != 'POST':
        form = ProdutoForm(instance=produto)
    else:
        #form = ProdutoForm(instance=produto, data=request.POST)
        file = request.FILES.get('imagem')  # O nome do campo deve corresponder ao nome no form
        form = ProdutoForm(instance=produto, data=request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.imagem = file  # Associa o arquivo manualmente
            produto.save()
            return HttpResponseRedirect(reverse('produto', args=[produto.id]))
    context = {'produto': produto, 'form': form}
    return render(request, 'market/editar_produto.html', context)

@login_required
@superuser_required
def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')  # Redireciona para a lista de produtos
    return render(request, 'market/confirmar_exclusao.html', {'produto': produto})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    usuario = request.user

    # Criar ou obter o carrinho do usuário
    carrinho, created = Carrinho.objects.get_or_create(usuario=usuario, ativo=True)

    # Adiciona o produto ao carrinho
    carrinho.adicionar_produto(produto)

    return redirect('index')

@login_required
def exibir_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user, ativo=True).first()
    return render(request, 'market/carrinho.html', {'carrinho': carrinho})

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho, Carrinho

@login_required
def excluir_produto_carrinho(request, produto_id):
    # Obtém o carrinho do usuário logado
    carrinho = get_object_or_404(Carrinho, usuario=request.user, ativo=True)

    # Verifica se o item do produto especificado está no carrinho
    item = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto_id=produto_id)

    if request.method == 'POST':
        if item.quantidade > 1:
            # Se a quantidade for maior que 1, diminui a quantidade
            item.quantidade -= 1
            item.save()  # Salva a alteração no banco de dados
        else:
            # Se a quantidade for igual a 1, remove o item do carrinho
            item.delete()
            
    return redirect('index')  # Redireciona caso não seja uma requisição POST

