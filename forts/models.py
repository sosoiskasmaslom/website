from django.db import models

class Fort(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='forts/static/images/', blank=True, null=True)
    text = models.TextField()

class Excursion(models.Model):
    title = models.CharField(max_length=50)
    meet_place = models.CharField(max_length=100)
    time = models.DateTimeField()
    count = models.PositiveSmallIntegerField()