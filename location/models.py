from django.db import models
from django.urls import reverse
# Create your models here.

class Location(models.Model):
    location_name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    location_state=models.CharField(max_length=200)
    location_country=models.CharField(max_length=200)
    location_description=models.CharField(max_length=255)
    location_Image=models.ImageField(upload_to='photos/locations')
    
    def get_url(self):
        return reverse('properties_by_location', args=[self.slug])

    def __str__(self):
        return self.location_name
