from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms

from .models import Event
from .models import Canton
from .models import Category


class EventListView(generic.ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = Event.dates()

        events = Event.objects.all()

        valid_events = {}
        for date in dates:
            valid_events[date]=[]
            for event in events:
                if event.is_date_valid(date) :
                    valid_events[date].append(event)

            if len(valid_events[date]) == 0:
                del valid_events[date]

        context['date_events'] = valid_events
        context['cantons'] = Canton.objects.all()
        context['categories'] = Category.objects.all()
        return context

class MyeventListView(generic.ListView):
    model = Event
    template_name = "home/myevent_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(fk_user=self.request.user)
        return context



class DateInput(forms.DateInput):
    input_type='date'

class EventCreateViewForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description','fk_address', 'date_begin', 'date_end', 'categories', 'image']
        widgets={'date_begin': forms.DateInput(attrs={'type':'date'}), 'date_end': forms.DateInput(attrs={'type':'date'})}

class EventCreateView(generic.CreateView):
    form_class = EventCreateViewForm
    model = Event
<<<<<<< HEAD
    success_url=reverse_lazy('index')
=======
    success_url = reverse_lazy('index')
>>>>>>> 5409c526aa4b6d2a627f8f20a26459a2951b7529

    def form_valid(self, form):
        Event = form.save(commit=False)
        Event.fk_user = self.request.user
        Event.save()
        return super().form_valid(form)
