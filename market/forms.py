from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'descricao', 'tag', 'preco', 'imagem']  # Incluindo todos os campos
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do produto',
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a quantidade',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do produto',
                'rows': 4,
            }),
            'tag': forms.Select(attrs={
                'class': 'form-control',
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o preço do produto',
                'step': '0.01',  # Permite decimais
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
        }