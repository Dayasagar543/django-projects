from django.db import models

# Create your models here.
class service(models.Model):
    service_icon=models.CharField(max_length=70)
    service_product=models.CharField(max_length=70)
    Sericce_product_description=models.TextField()