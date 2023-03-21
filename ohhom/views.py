from django.http import HttpResponse
from django.shortcuts import render
from agency.models import Property
from location.models import Location
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    properties=Property.objects.all().filter(is_avalible=True)
    locations=Location.objects.all()
    context = {
        'properties':properties,
        'locations':locations,
    }
    
    return render(request,'home.html',context)

