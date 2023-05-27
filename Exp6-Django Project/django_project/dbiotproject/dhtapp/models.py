from django.db import models

# Create your models here.


class dht(models.Model):

    temp =models.TextField(max_length=64)
    hum= models.TextField(max_length=46)



