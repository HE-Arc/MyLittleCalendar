from django.contrib import admin

# Register your models here.
from .models import Event, Address, Canton, Category

# Register your models here.

admin.site.register(Event)
admin.site.register(Canton)
admin.site.register(Address)
admin.site.register(Category)
