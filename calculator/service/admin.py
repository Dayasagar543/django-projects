from django.contrib import admin
from service.models import service

class admin_service(admin.ModelAdmin):
    list_display=('service_icon','service_product','Sericce_product_description')

admin.site.register(service,admin_service   )
# Register your models here.
