from django.db import models
from django.conf import settings

# Create your models here.
class OrdemProducao(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ordens')
    
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)  
    
    def __call__(self, *args, **kwds):
        return f"Ordem: {self.produto} - Qtde: {self.quantidade} - owner: {self.owner.username}"