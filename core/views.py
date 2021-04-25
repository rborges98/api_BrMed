import requests
from django.http import JsonResponse


def index(request, ano, mes, dia): #recebe o request da url e as variaveis p/ adicionar ao link da api

    try:
        response = requests.get(
            'https://api.vatcomply.com/rates?date='+ano+'-'+mes+'-'+dia+'&base=BRL'
            )

        json = response.json() #gera o json

    except:
        json = {'error':'error'}

    return JsonResponse(json) #retorna o json no endpoint