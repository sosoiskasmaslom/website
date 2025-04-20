from django.db import models
from registration.models import User

class Fort(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='forts/static/images/', blank=True, null=True)
    text = models.TextField()

class Excursion(models.Model):

    title = models.CharField(max_length=50)
    meet_place = models.CharField(max_length=100)
    time = models.DateTimeField()
    count = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
