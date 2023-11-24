from django.db import models
from datetime import datetime


class Fotografia(models.Model):
    OPCOES_DE_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
        
        
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=200, choices=OPCOES_DE_CATEGORIA ,default='')
    descricao = models.TextField(max_length=500, null=False, blank=False)  
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False) 
    
    
    
    def __str__(self) -> str:
        return self.nome