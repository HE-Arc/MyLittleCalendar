from django.urls import path
from django.contrib import admin

from home import views
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('', views.EventListView.as_view(),name='index'),
    path('new/', views.EventCreateView.as_view(), name='event-new'),
    path('event/', views.MyeventListView.as_view(), name='my-events'),
    url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)),]+urlpatterns
