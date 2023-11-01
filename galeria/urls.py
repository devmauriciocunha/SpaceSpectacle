from django.urls import path
from galeria.views import index

#Vamos primeiro criar uma lista

urlpatterns = [
    path('', index)
]
