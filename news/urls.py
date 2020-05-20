from django.urls import path
from . import views
from .views import listaArticoliView, listaGiornalistiView, articoliGiorn


app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),  
    path('lista-articoli/', listaArticoliView.as_view(), name='articoli'),
    path('leggi-articoli/<int:pk>', articoliGiorn, name='articoli2'),
    path('lista-giornalisti/', listaGiornalistiView.as_view(), name='giornalisti'),
]