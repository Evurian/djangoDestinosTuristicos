# destinos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_destinos, name='lista_destinos'),
    path('añadir/', views.añadir_destino, name='añadir_destino'),
    path('modificar/<int:pk>/', views.modificar_destino, name='modificar_destino'),
    path('eliminar/<int:pk>/', views.eliminar_destino, name='eliminar_destino'),
]
