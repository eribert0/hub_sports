from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# https://api.api-futebol.com.br/v1/

def futebol_home(request):
    return render(request, 'home.html')

def futebol_campeonatos(request):
    url = 'https://api.api-futebol.com.br/v1/campeonatos'
    headers = {
        'Authorization': 'Bearer live_b03f8374826632e4e1a376d7320f52'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        campeonatos = response.json()

        for campeonato in campeonatos:
            campeonato['link'] = campeonato.pop('_link', None)
    else:
        campeonatos = []
        
    return render(request, 'campeonatos.html', {'campeonatos':campeonatos})

def campeonato_detalhes(request, campeonato_id):
    url = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}'
    headers = {
        'Authorization':'Bearer live_b03f8374826632e4e1a376d7320f52'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        campeonato = response.json()
    else:
        campeonato = {}

    return render(request, 'campeonato_detalhes.html', {'campeonato':campeonato})
