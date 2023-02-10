from django.http import HttpResponse
from django.shortcuts import render
from agency.models import Property
def home(request):
    properties=Property.objects.all().filter(is_avalible=True)

    context = {
        'properties':properties,
    }
    return render(request,'home.html',context)
