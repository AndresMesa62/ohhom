from django.contrib import admin
from .models import Location
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('location_name','location_state','location_country')}
    list_display = ('location_name','location_state','location_country')
admin.site.register(Location,LocationAdmin)