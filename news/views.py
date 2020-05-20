from django.shortcuts import render,redirect
from .models import newsArticoliModels, newsGiornalistiModels
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request): 
    return render(request, "home.html")

class listaArticoliView(ListView):
    model = newsArticoliModels #modello dei dati da utilizzare 
    template_name = "news/articoli.html"  #pagina per mostrare i dati

class listaGiornalistiView(ListView):
    model = newsGiornalistiModels #modello dei dati da utilizzare 
    template_name = "news/giornalisti.html"  #pagina per mostrare i dati

def articoliGiorn(request, pk): #metodo per la gestione del pk, non è completo ma non sono riuscito a terminarlo
    post = get_object_or_404(newsArticoliModels, id=pk)
    model = newsArticoliModels
    return render(request, 'news/articoli.html')
