from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rota-protegida/', views.rota_protegida, name='rota-protegida')
]
