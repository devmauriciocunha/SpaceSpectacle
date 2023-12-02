from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro
 
from . import views   
    

#Vamos primeiro criar uma lista

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path("nova-imagem", nova_imagem, name="nova_imagem"),
    path('editar-imagem/<int:foto_id>/', views.editar_imagem, name='editar_imagem'),
    path("deletar-imagem/<int:foto_id>/", views.deletar_imagem, name="deletar_imagem"),
    path('filtro/<str:categoria>/', views.filtro, name='filtro'),
]


