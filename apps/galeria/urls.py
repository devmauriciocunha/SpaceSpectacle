from django.urls import path
from galeria.views import index, imagem, buscar
from .views import imagem
#Vamos primeiro criar uma lista

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
]

