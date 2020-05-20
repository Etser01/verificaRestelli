from django.shortcuts import render,HttpResponse
import datetime

def home(request): 
    return render(request, "home.html")