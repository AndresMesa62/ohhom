from django.http import HttpResponse
from django.shortcuts import render
from agency.models import Property
from location.models import Location
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .graficas import Grafica as g
import pandas as pd

df = pd.read_csv('ohhom/ohhom/datos.csv')
        
g.mapaCalor(df)
def home(request):
    properties=Property.objects.all().filter(is_avalible=True)
    locations=Location.objects.all()
    context = {
        'properties':properties,
        'locations':locations,
    }
    
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')

def newdata(request):
    return render(request,'datos.html')
