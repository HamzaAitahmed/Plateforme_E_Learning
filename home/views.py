from django.shortcuts import render
from .models import *


def cls(request):
    return render(request, "plat/class.html", {})


def list_client(request):
    lc = Client.objects.all()
    return render(request, 'plat/login.html', {'lc': lc})


def login(request):
    lc = Client.objects.all()
    cr = Cour.objects.all()
    return render(request, "plat/login.html", {'lc': lc, 'cr': cr})


def home(request):
    return render(request, "plat/hm.html", {})


def about(request):
    return render(request, "plat/about.html", {})


def contact(request):
    return render(request, "plat/contact.html", {})


def remarque(request):
    return render(request, "plat/remarque.html", {})


def admin(request):
    return render(request, "admin", {})

