from django.contrib import admin
from .models import * # Added manually
# Register your models here.
admin.site.register(Car_make)
admin.site.register(Car)