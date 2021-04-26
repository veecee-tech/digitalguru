from django.contrib import admin
from .models import Service
# Register your models here.



class ServiceModel(admin.ModelAdmin):
    list_display = ('service_name', 'service_desc', 'service_img')
    list_editable = ('service_desc',)



admin.site.register(Service, ServiceModel)
