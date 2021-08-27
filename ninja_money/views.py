from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def inicio(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
    return render(request, 'index.html')

def process_money(request):
    if "farm" in request.POST: #Si en el POST viene "farm"...
        farmPrize = randint(10, 20) #Valor aleatorio entre 10 y 20
        request.session['gold_amount'] += farmPrize #Se suma el valor a la variable de la sesion

    if "cave" in request.POST: #Si en el POST viene "cave"...
        cavePrize = randint(5, 10)
        request.session['gold_amount'] += cavePrize

    if "house" in request.POST: #Si en el POST viene "house"...
        housePrize = randint(5, 10)
        request.session['gold_amount'] += housePrize

    if "casino" in request.POST: #Si en el POST viene "casino"...
        request.session['gold_amount'] += randint(-50, 50)

    return redirect('/')