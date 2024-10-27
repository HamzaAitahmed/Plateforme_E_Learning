from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Parent_name', 'email', 'password', 'Child_name', 'Child_age', 'message')
    list_filter = ('Parent_name', 'Child_name')
    search_fields = ('Parent_name', 'email')


@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'client', 'Date')
    list_filter = ('category', 'client')
    search_fields = ('category', 'client')
    raw_id_fields = ('client',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'Video_Category', )
    list_filter = ('Video_Category', )
    search_fields = ('title', 'Video_Category',)
