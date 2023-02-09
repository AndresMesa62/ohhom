from django.contrib import admin
from .models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('is_avalible','property_name','category','municipality','area','price','created_date','is_verified')
    list_display_links = ('property_name',)
    prepopulated_fields = {'slug':('property_name',)}

admin.site.register(Property,PropertyAdmin)