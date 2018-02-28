from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from home import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
