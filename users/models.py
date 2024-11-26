from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Modelo Usuario
class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    celular = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField()
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
