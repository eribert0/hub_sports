from django.urls import path
from . import views

urlpatterns = [
    path('', views.futebol_home, name='futebol-home'),
    path('brasileirao/', views.liga_brasileirao, name='liga-brasileirao') 
]