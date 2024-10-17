from django.views.generic import TemplateView
from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [

    # URLS basés sur les Templates
    path('', TemplateView.as_view(template_name='plat/login.html'), name="login"),
    path('home', views.home, name="home"),
    path('class', views.cls, name="cls"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('appointment', views.remarque, name="remarque"),
]
