from django.http import HttpResponse
from django.shortcuts import render
from agency.models import Property
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    properties=Property.objects.all().filter(is_avalible=True)
    context = {
        'properties':properties,
    }
    
    return render(request,'home.html',context)

