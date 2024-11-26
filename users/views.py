from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('/market/templates/market/index')  # Redirecione para a página principal
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
