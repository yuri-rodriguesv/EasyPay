from django.shortcuts import render
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.urls import reverse
def index(request):
    produtos = Produto.objects.all()  # Busca todos os produtos
    context = {'produtos': produtos}
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

def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')  # Redireciona para a lista de produtos
    return render(request, 'market/confirmar_exclusao.html', {'produto': produto})