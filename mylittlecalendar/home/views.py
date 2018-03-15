from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
#from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from .models import Event


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

        return context

class DateInput(forms.DateInput):
    input_type='date'

class EventCreateViewForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date_begin', 'date_end', 'categories', 'image']
        widgets={'date_begin': forms.DateInput(attrs={'type':'date'})}

class EventCreateView(generic.CreateView):
    form_class = EventCreateViewForm
    model = Event
    # fields = ['name', 'description', 'date_begin', 'date_end', 'categories', 'image']
    # success_url = reverse_lazy('index')
    #
    # def get_form(self, form_class=None):
    #     form = super(EventCreateView, self).get_form(form_class)
    #     form.flieds['date_begin'].widget.attrs.update({'class': 'datepicker'})
    #     return form
    #widgets={'date_begin': forms.DateInput(attrs={'class':'datepicker'})}
