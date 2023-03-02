from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def greet(request, name: str):
    return render(request, 'greet.html',
       {'name': name.capitalize()}
    )

def horas():
    from datetime import datetime

    agora = datetime.now()
    hora = agora.strftime("%H")

    if int(hora) <= 18:
        return True
    else:
        return False

def tia_do_zap(request, name: str,):
    return render(request, 'tia_do_zap.html', 
        {'name': name.capitalize(),
         'dia': horas()
        }
    )
