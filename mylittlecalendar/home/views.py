from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Event


class EventListView(generic.ListView):
    model = Event


class EventCreateView(generic.CreateView):
    model = Event
    fields = ['name', 'description', 'date_begin', 'date_end', 'categories', 'image']
    success_url = reverse_lazy('dashboard-events')
