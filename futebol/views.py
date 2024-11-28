from django.shortcuts import render
from django.http import HttpResponse

def futebol_home(request):
    return HttpResponse('Página Home - Futebol')

def liga_brasileirao(request):
    return HttpResponse('Brasileirão Séria A')
