
from django.urls import path
from . import views

urlpatterns = [
   path('', views.agency, name='agency'),
   path('<slug:category_slug>/', views.agency, name='properties_by_category'),
   path('location/<slug:location_slug>/', views.agency, name='properties_by_location'),
   path('<slug:category_slug>/<slug:property_slug>/', views.property_detail, name='property_detail'),
]

