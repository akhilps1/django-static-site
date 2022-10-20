from django.db import models

# Create your models here.


class Place(models.Model):
    place_name = models.CharField(max_length=250)
    place_image = models.ImageField(upload_to='placeImages')
    place_des = models.TextField()


class Teams(models.Model):
    team_name = models.CharField(max_length=250)
    team_image = models.ImageField(upload_to='teamImages')
    team_des = models.TextField()
