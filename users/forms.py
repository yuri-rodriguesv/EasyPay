from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'Email',
            'password': 'Senha'
        }