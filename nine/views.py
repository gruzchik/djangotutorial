from django.shortcuts import render
from django.http import HttpResponse
from nine.models import Heroes

# Create your views here.


def index(request):
    return HttpResponse("Hello world.")

def square(request):
    return render(request, 'nine/square.html',{'a': square.a})

def heroes(request):
    heros = Heroes('nine/data.csv')
    return render(request, 'nine/heroes.html', {'model': heros})


def heroes_details(request, nickname):
    heros = Heroes('nine/data.csv')
    hero = heros.get_hero(nickname)
    if nickname == 'None':
       return HttpResponse('hero not found')
    else:
        return render(request, 'nine/details.html', {'model': hero})    
