from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date_begin=models.DateField()
    date_end=models.DateField()
    fk_adress=models.ForeignKey('Adress', on_delete=models.CASCADE)
    fk_user=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    image=models.ImageField(upload_to = 'event_imgs', default = 'event_imgs/default.jpg')


class Canton(models.Model):
    name=models.CharField(max_length=100)

class Adress(models.Model):
    npa=models.CharField(max_length=20)
    locality=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    fk_canton=models.ForeignKey('Canton', on_delete=models.CASCADE)
