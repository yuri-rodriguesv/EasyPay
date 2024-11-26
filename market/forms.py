from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'descricao', 'imagem']  # Incluindo apenas os campos que deseja no formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do produto'}),
        }