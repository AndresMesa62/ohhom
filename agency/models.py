from django.db import models
from category.models import category

# Create your models here.


class Property(models.Model):
    
    #general
    property_name = models.CharField(max_length=200)
    slug          = models.SlugField(max_length=200)
    description   = models.TextField(max_length=500,blank=True)
    price         = models.IntegerField()
    images        = models.ImageField(upload_to='photos/properties')
    category      = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    #owner
    owner         = models.CharField(max_length=200,default='Ohom')
    owner_id      = models.CharField(max_length=200,default='Ohom')
    owner_email   = models.CharField(max_length=200,default='ohom.adm@gmail.com')
    #ubication
    address       = models.CharField(max_length=200,unique=True)
    municipality  = models.CharField(max_length=200)
    state         = models.CharField(max_length=200)
    country       = models.CharField(max_length=200)
    
    #Aditional information
    is_verified            = models.BooleanField(default=False)
    area                   = models.IntegerField()
    rooms                  = models.IntegerField()
    bathrooms              = models.IntegerField()
    dining_room            = models.IntegerField()
    floor                  = models.IntegerField()
    is_avalible            = models.BooleanField(default=True)
    allows_pets            = models.BooleanField(default=False)
    allows_kids            = models.BooleanField(default=False)
    has_motorcycle_parking = models.BooleanField(default=False)
    has_car_parking        = models.BooleanField(default=False)
    has_garden             = models.BooleanField(default=False)
    has_elevator           = models.BooleanField(default=False)
    has_security           = models.BooleanField(default=False)
    has_pool               = models.BooleanField(default=False)
    has_gym                = models.BooleanField(default=False)
    has_integral_kitchen   = models.BooleanField(default=False)
    has_closets            = models.BooleanField(default=False)

    #multimedia
    maps_url               = models.URLField(default='https://www.google.com/maps/?hl=es')
    video360_url           = models.URLField(default='https://www.youtube.com/?hl=es&gl=EC')
    videoblog_url          = models.URLField(default='https://www.youtube.com/?hl=es&gl=EC')

    def __str__(self):
        return self.property_name
    
