from django.urls import path
from . import views

urlpatterns = [
    path('', views.futebol_home, name='futebol-home'),
    path('campeonatos/', views.futebol_campeonatos, name='campeonatos'),
    path('campeonatos/<int:campeonato_id>', views.campeonato_detalhes, name='campeonato-detalhes'),
    
]