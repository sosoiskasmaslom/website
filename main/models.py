from django.db import models

class Adj(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=250, default="") 
    image = models.ImageField(upload_to='forts/static/adj/', blank=True, null=True)
    text = models.TextField()
