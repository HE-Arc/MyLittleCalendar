from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date, datetime
from django.db.models import Max
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date_begin=models.DateField()
    date_end=models.DateField()
    fk_address=models.ForeignKey('address', on_delete=models.CASCADE)
    fk_user=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    image=models.ImageField(upload_to = 'images/events', default = 'images/events/default.jpg')



    def dates():
        end_date = Event.objects.all().aggregate(Max('date_end'))['date_end__max']

        if end_date is None:
            return "1900-01-01"

        dates = []
        start_date = date.today()

        date_range = []
        for n in range(int (((end_date+timedelta(1)) - start_date).days)):
            date_range.append(start_date + timedelta(n))

        for single_date in date_range:
            dates.append(single_date.strftime("%Y-%m-%d"))

        return dates

    def __str__(self):
        return self.name

    def is_date_valid(self, date_test):
        return date_test <= self.date_end.strftime("%Y-%m-%d") and date_test >= self.date_begin.strftime("%Y-%m-%d")


class Canton(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Address(models.Model):
    npa=models.CharField(max_length=20)
    locality=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    fk_canton=models.ForeignKey('Canton', on_delete=models.CASCADE)

    def __str__(self):
        return self.street
