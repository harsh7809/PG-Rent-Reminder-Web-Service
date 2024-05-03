from django.db import models


# Create your models here.
class Contact(models.Model):
    mesasge=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    date=models.DateField()
