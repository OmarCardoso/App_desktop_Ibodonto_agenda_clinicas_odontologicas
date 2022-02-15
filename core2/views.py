from django.shortcuts import render, HttpResponse, redirect
from core2.models import Evento
# Create your views here.

#def eventos(request, titulo_evento):
#    Evento.objects.get(titulo = titulo_evento)
#    return HttpResponse(Evento.local)

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def index(request):
    return redirect('/agenda/')