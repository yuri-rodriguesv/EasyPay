from django.db import models
#from users.models import Usuario
# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='produtos_imagens/', null=True, blank=True)  # Novo campo

    def __str__(self):
        return self.nome