from django.db import models
from category.models import category
from django.urls import reverse
# Create your models here.


class Property(models.Model):
    
    #general
    property_name = models.CharField(max_length=200)
    slug          = models.SlugField(max_length=200,unique=True)
    description   = models.TextField(max_length=500,blank=True)
    price         = models.IntegerField()
    category      = models.ForeignKey(category, on_delete=models.CASCADE)
    
    images        = models.ImageField(upload_to='photos/properties')
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
    floor                  = models.IntegerField()
    
    #Aditional information disponibility
    is_verified            = models.BooleanField(default=False)
    is_avalible            = models.BooleanField(default=True)

    #about property
    area                   = models.IntegerField()
    number_of_rooms        = models.IntegerField()
    number_of_bathrooms    = models.IntegerField()
    has_dining_room        = models.BooleanField(default=False)
    has_integral_kitchen   = models.BooleanField(default=False)
    has_work_zone          = models.BooleanField(default=False)
    has_hall               = models.BooleanField(default=False)
    has_study              = models.BooleanField(default=False)
    has_balcony_or_terrace = models.BooleanField(default=False)
    number_of_balcony_or_terrace = models.IntegerField()
    has_pool               = models.BooleanField(default=False)
    has_parkland           = models.BooleanField(default=False)
    has_pet_area           = models.BooleanField(default=False)
    has_gym                = models.BooleanField(default=False)
    has_motorcycle_parking = models.BooleanField(default=False)
    has_car_parking        = models.BooleanField(default=False)
    has_concierge          = models.BooleanField(default=False)
    has_doorman            = models.BooleanField(default=False)
    has_elevator           = models.BooleanField(default=False)
    
    #about services
    has_wifi               = models.BooleanField(default=False)
    has_air_conditioning   = models.BooleanField(default=False)
    has_hot_water          = models.BooleanField(default=False)
    has_security_cameras   = models.BooleanField(default=False)
    has_smoke_detector     = models.BooleanField(default=False)
    
    #about furniture
    has_coffee_maker       = models.BooleanField(default=False)
    has_dishwasher         = models.BooleanField(default=False)
    has_oven               = models.BooleanField(default=False)
    has_plates_and_cutlery = models.BooleanField(default=False)
    has_microwave          = models.BooleanField(default=False)
    has_freezer            = models.BooleanField(default=False)
    
    has_clothes_iron       = models.BooleanField(default=False)
    has_washing_machine    = models.BooleanField(default=False)
    has_dryer              = models.BooleanField(default=False)
    
    has_towels             = models.BooleanField(default=False)
    has_soap               = models.BooleanField(default=False)
    has_toilet_paper       = models.BooleanField(default=False)
    has_hair_dryer         = models.BooleanField(default=False)
    has_bed_sheets         = models.BooleanField(default=False)
    
    has_tv                 = models.BooleanField(default=False)
    number_of_tvs          = models.IntegerField()
    has_bed                = models.BooleanField(default=False)
    number_of_beds         = models.IntegerField()
    has_closet             = models.BooleanField(default=False)
    number_of_closets      = models.IntegerField()

    #our opinion
    
    why_this_place          = models.TextField(max_length=500,blank=True)
    about_transportation    = models.TextField(max_length=500,blank=True)
    for_students            = models.TextField(max_length=500,blank=True)

    #rules

    allows_pets             = models.BooleanField(default=False)
    allows_smokers          = models.BooleanField(default=False)
    allows_parties          = models.BooleanField(default=False)

    #multimedia
    maps_url               = models.URLField(default='https://www.google.com/maps/?hl=es',max_length=400)
    video360_url           = models.URLField(default='https://www.youtube.com/?hl=es&gl=EC',max_length=400)
    videoblog_url          = models.URLField(default='https://www.youtube.com/?hl=es&gl=EC',max_length=400)

    def get_url(self):
        return reverse('property_detail',args=[self.category.slug, self.slug])

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.property_name
    
