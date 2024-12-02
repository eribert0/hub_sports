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
    url_tabela = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela'
    url_artilharia = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/artilharia'
    headers = {
        'Authorization':'Bearer live_b03f8374826632e4e1a376d7320f52'
    }

    response_tabela = requests.get(url_tabela, headers=headers)
    response_artilharia = requests.get(url_artilharia, headers=headers)

    if response_tabela.status_code == 200 and response_artilharia.status_code == 200:
        tabela = response_tabela.json()
        artilharia = response_tabela.json()
    else:
        tabela = []
        artilharia = []

    return render(request, 'campeonato_detalhes.html', {
        'tabela':tabela,
        'artilheiros': artilharia
    })
