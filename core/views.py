import requests
from django.http import JsonResponse


def index(request, date_url): #recebe o request da url e as variaveis p/ adicionar ao link da api


        response = requests.get(
            'https://api.vatcomply.com/rates?date='+date_url+'&base=BRL'
            )

        json = response.json()

        return JsonResponse(json) #retorna o json no endpoint