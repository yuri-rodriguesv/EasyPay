from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'cpf', 'celular', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Senha'
        }