from django.urls import path
from galeria.views import index, imagem
from .views import imagem
#Vamos primeiro criar uma lista

urlpatterns = [
    path('', index),
    path('imagem.html/', imagem, name='imagem'),
]

