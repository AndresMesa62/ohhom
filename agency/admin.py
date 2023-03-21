from django.contrib import admin
from .models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('is_avalible','property_name','category','location','area','price','created_date','is_verified')
    list_display_links = ('property_name',)
    prepopulated_fields = {'slug':('property_name','price','location', 'number_of_bathrooms', 'number_of_beds', 'number_of_closets', 'number_of_rooms', 'number_of_tvs')}

admin.site.register(Property,PropertyAdmin)