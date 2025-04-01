
from django.db import models
 
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.BinaryField(max_length=100)
    birth_date = models.DateField()
    # log_date = models.DateTimeField()