
from django.urls import path
from . import views

urlpatterns = [
   path('', views.agency, name='agency'),
]

