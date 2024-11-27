from django.db import models
from users.models import Usuario  
class Produto(models.Model):
    TAG_CHOICES = [
        ('salgado', 'Salgado'),
        ('doce', 'Doce'),
        ('bebida', 'Bebida'),
        ('bala', 'Bala'),
    ]

    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='produtos_imagens/', null=True, blank=True)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES, default='salgado')
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Definindo valor padrão
    
    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    produtos = models.ManyToManyField(Produto, through='ItemCarrinho')
    
    def adicionar_produto(self, produto):
        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=self,
            produto=produto,
            defaults={'preco': produto.preco}
        )
        if not created:
            item.quantidade += 1
            item.save()

    @property
    def total(self):
        return sum(item.subtotal for item in self.itemcarrinho_set.all())

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco




