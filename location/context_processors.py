from .models import Location

def Locations_links(request):
    links=Location.objects.all()
    return dict(location_links=links)