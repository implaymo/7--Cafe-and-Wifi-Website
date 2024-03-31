from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False)
    map_url = models.CharField(max_length=500, null=False)
    img_url = models.CharField(max_length=500, null=False)
    location = models.CharField(max_length=250, null=False)
    seats = models.CharField(max_length=250, null=False)
    has_toilet = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_sockets = models.BooleanField(default=False)
    can_take_calls = models.BooleanField(default=False)
    coffee_price = models.CharField(max_length=250, null=True)
    

