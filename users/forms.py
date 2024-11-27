from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'cpf', 'celular', 'password1', 'password2']
        labels = {
            'username': 'Nome do Usuario',
            'email': 'E-mail',
            'cpf': 'CPF',
            'celular': 'Celular',
            'password1': 'Senha',
            'password2': 'Confirmar Senha'
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Senha'
        }

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Usa o modelo de usuário atual (padrão ou personalizado)
        fields = ['username', 'email', 'celular']  # Adicione os campos que podem ser editados
        labels = {
            'username': 'Nome do Usuário',
            'email': 'E-mail',
            'celular': 'Celular',
        }
        widgets = {
            'celular': forms.TextInput(attrs={'maxlength': '11', 'placeholder': 'Ex: 11999999999'}),
        }
