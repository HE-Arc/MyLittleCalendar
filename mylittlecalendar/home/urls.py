from django.urls import path
from django.contrib import admin

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
