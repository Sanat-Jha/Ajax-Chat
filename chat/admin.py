from django.contrib import admin
from django.http.response import JsonResponse
from .models import Room

# Register your models here.
admin.site.register(Room)