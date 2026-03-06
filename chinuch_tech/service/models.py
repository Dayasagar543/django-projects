from django.db import models

# Create your models here.
class User_data(models.Model):
    First_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    