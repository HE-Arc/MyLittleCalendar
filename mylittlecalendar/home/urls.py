from django.urls import path
from django.contrib import admin

from home import views

urlpatterns = [
    path('', views.EventListView.as_view(),name='index'),
]
