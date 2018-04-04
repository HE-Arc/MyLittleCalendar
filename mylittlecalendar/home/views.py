from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms
import django_filters
#from .filters import EventFilter

from .models import Event
from .models import Canton
from .models import Category
from .models import Address

# View for the list of events
class EventListView(generic.ListView):
    model = Event

    def get_context_data(self, **kwargs):
        """Return a dictionnary with a date key containing all events present that day"""
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

# View for the list of events of the authenticated user
class MyeventListView(generic.ListView):
    model = Event
    template_name = "home/myevent_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(fk_user=self.request.user)
        return context

class DateInput(forms.DateInput):
    input_type='date'


# View to create a new event
class EventCreateViewForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description','fk_address', 'date_begin', 'date_end', 'categories', 'image']
        widgets={'date_begin': forms.DateInput(attrs={'type':'date'}), 'date_end': forms.DateInput(attrs={'type':'date'})}

class EventCreateView(generic.CreateView):
    form_class = EventCreateViewForm
    model = Event
    success_url = reverse_lazy('my-events')

    def form_valid(self, form):
        Event = form.save(commit=False)
        Event.fk_user = self.request.user
        Event.save()
        return super().form_valid(form)


# View for the search of events
class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantons = django_filters.ModelMultipleChoiceFilter(queryset=Canton.objects.all(), widget=forms.CheckboxSelectMultiple,label="Canton" )

    class Meta:
        model = Event
        fields = ['name', 'date_begin', 'date_end', 'categories', 'cantons']
        widgets={'date_begin': django_filters.DateFromToRangeFilter(attrs={'type':'date'}), 'date_end': django_filters.DateFromToRangeFilter(attrs={'type':'date'})}

def search(request):
    event_list = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset=event_list)
    return render(request, 'home/event_search.html', {'filter': event_filter})


# View for updating an event
class EventUpdateView(generic.UpdateView):
    model = Event
    form_class = EventCreateViewForm
    success_url = reverse_lazy('my-events')

# View for deleting an event
class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('my-events')


# View to create a new address
class AddressCreateView(generic.CreateView):
    model = Address
    fields = ['npa', 'locality','street', 'fk_canton']
    success_url = reverse_lazy('my-events')
