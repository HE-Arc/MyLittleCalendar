from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date, datetime
from django.db.models import Max
from django import forms

# Create your models here.

# Model for the categories
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for the events
class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date_begin=models.DateField(verbose_name= 'Start date')
    date_end=models.DateField(verbose_name= 'End date')
    fk_address=models.ForeignKey('address', on_delete=models.CASCADE,verbose_name= 'Address')
    fk_user=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name= 'Category')
    image=models.ImageField(upload_to = 'images/events', default = 'images/events/default.jpg')

    def dates():
        """Creates all dates needed"""
        end_date = Event.objects.all().aggregate(Max('date_end'))['date_end__max']

        if end_date is None:
            return "01.01.1900"

        dates = []
        start_date = date.today()

        for n in range(int (((end_date+timedelta(1)) - start_date).days)):
            dates.append((start_date + timedelta(n)).strftime("%d.%m.%Y"))

        return dates

    def __str__(self):
        return self.name

    def is_date_valid(self, date_test):
        """Tests if the date given is between today and its date_end"""
        return datetime.strptime(date_test, '%d.%m.%Y').date() <= self.date_end and datetime.strptime(date_test, '%d.%m.%Y').date() >= self.date_begin

# Model for the region
class Canton(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for the address
class Address(models.Model):
    npa=models.CharField(max_length=20)
    locality=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    fk_canton=models.ForeignKey('Canton', on_delete=models.CASCADE, verbose_name= 'Canton')

    def __str__(self):
        return '%s - %s %s %s' %(self.fk_canton, self.npa, self.locality, self.street)
