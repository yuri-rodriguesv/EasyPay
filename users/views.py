from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm, EditarUsuarioForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'users/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')  # Redirecione para a página principal
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def editar_perfil(request):
    usuario = request.user  # Obtém o usuário logado
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)  # Usa os dados enviados e o usuário atual
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            messages.success(request, 'Suas informações foram atualizadas com sucesso!')
            return redirect('editar_perfil')  # Redireciona para a página de edição ou outra página
        else:
            messages.error(request, 'Erro ao atualizar suas informações. Verifique os dados informados.')
    else:
        form = EditarUsuarioForm(instance=usuario)  # Preenche o formulário com os dados do usuário atual
    
    return render(request, 'users/editar_perfil.html', {'form': form, 'usuario': usuario})