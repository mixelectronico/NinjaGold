from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.

def inicio(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
        request.session['moves'] = []
    return render(request, 'index.html')

def process_money(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    if "farm" in request.POST: #Si en el POST viene "farm"...
        farmPrize = randint(10, 20) #Valor aleatorio entre 10 y 20
        request.session['gold_amount'] += farmPrize
        request.session['moves'].append([farmPrize, 'farm', time]) #Se suma el valor a la variable de la sesion

    if "cave" in request.POST: #Si en el POST viene "cave"...
        cavePrize = randint(5, 10)
        request.session['gold_amount'] += cavePrize
        request.session['moves'].append([cavePrize, 'cave', time])

    if "house" in request.POST: #Si en el POST viene "house"...
        housePrize = randint(5, 10)
        request.session['gold_amount'] += housePrize
        request.session['moves'].append([housePrize, 'house', time])

    if "casino" in request.POST: #Si en el POST viene "casino"...
        casinoPrize = randint(-50, 50)
        request.session['gold_amount'] += casinoPrize
        request.session['moves'].append([casinoPrize, 'casino', time])

    return redirect('/')