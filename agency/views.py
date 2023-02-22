from django.shortcuts import render, get_object_or_404
from .models import Property
from category.models import category
# Create your views here.

def agency(request,category_slug=None):
    categories=None
    properties=None

    if category_slug!=None:
        categories=get_object_or_404(category, slug=category_slug)
        properties=Property.objects.filter(category=categories,is_avalible=True)
        property_count=properties.count()
    else:
        properties=Property.objects.all().filter(is_avalible=True)
        property_count=properties.count()
    context = {
        'properties':properties,
        'property_count':property_count,
    }
    return render(request,'agency/agency.html',context)

def property_detail(request, category_slug, property_slug):
    try:
        single_property=Property.objects.get(category__slug=category_slug,slug=property_slug)
    except Exception as e:
        raise e
    context = {
        'single_property':single_property,
    }
    return render(request,'agency/property_detail.html',context)