from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('Parent_name', 'email', 'Child_name', 'Child_age')
    list_filter = ('Parent_name', 'Child_name')
    search_fields = ('Parent_name', 'email')


@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
    list_display = ('category', 'client', 'Date')
    list_filter = ('category', 'client')
    search_fields = ('category', 'client')
    raw_id_fields = ('client',)
