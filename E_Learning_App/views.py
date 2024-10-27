from django.db.models import Q
from django.shortcuts import render
from .models import *

user = None


def signup(request):
    error = False
    message = ""
    if request.method == 'POST':
        password = request.POST['psw']
        repassword = request.POST['rpsw']
        email = request.POST['eml']
        parent_name = request.POST['pname']
        child_name = request.POST['cname']
        child_age = request.POST['cage']
        new_member = Client(Parent_name=parent_name, password=password, email=email, Child_name=child_name,
                            Child_age=child_age, message=None)

        client = Client.objects.filter(Q(email=email)).first()
        if client:
            error = True
            message = f"ERROR !!! {email} already Existe !!! "

        if not error:
            if password != repassword:
                error = True
                message = "Password Confirmation doesn't match"

        t = {'email': email, 'error': error, 'message': message}
        if error:
            return render(request, "login.html", t)
        else:
            new_member.save()
            return render(request, "seconnecter.html", t)
    return render(request, "login.html")


def signin(request):
    users = Client.objects.all()
    error = True
    if request.method == 'POST':
        password = request.POST['psw']
        email = request.POST['eml']

        client = Client.objects.filter(email=email).first()
        global user
        user = email

        if client:
            auth_user = False
            if password == client.password:
                auth_user = True
                error = False

            if auth_user:
                return render(request, 'main.html', {'client': client, 'users': users})
            else:
                message = "Password Doesn't Match !!! "
                return render(request, 'seconnecter.html', {'error': error, 'message': message})
        else:
            message = email+" Doesn't Existe !!! "
            return render(request, 'seconnecter.html', {'error': error, 'message': message})


def msg(request):
    error = True
    if request.method == 'POST':
        error2 = True
        message = request.POST['message']
        for i in message:
            if i != ' ':
                error2 = False
                break
        if error2:
            message = None

        Client.objects.filter(email=user).update(message=message)
        client = Client.objects.filter(email=user).first()
        return render(request, "remarque.html", {'client': client})
    return render(request, "login.html", {'error': error})


def join_int(request):
    cour = Cour.objects.filter(category="Interactive")
    video = Video.objects.filter(Video_Category="Interactive")
    category = "Interactive"
    client = Client.objects.filter(Q(email=user)).first()
    print(client)
    for x in cour:
        if x.client == client:
            return render(request, "videos.html", {'client': client, 'video': video, 'category': category})
    if request.method == 'POST':

        new_member = Cour(client=client, category="Interactive", Date=timezone.now())
        new_member.save()
        return render(request, "videos.html", {'client': client, 'video': video, 'category': category})

    return render(request, "videos.html", {'client': client, 'video': video, 'category': category})


def join_alp(request):
    cour = Cour.objects.filter(category="Alphabet")
    video = Video.objects.filter(Video_Category="Alphabet")
    category = "Alphabet"
    client = Client.objects.filter(Q(email=user)).first()
    for x in cour:
        if x.client == client:
            return render(request, "videos.html", {'client': client, 'video': video, 'category': category})

    if request.method == 'POST':
        new_member = Cour(client=client, category="Alphabet", Date=timezone.now())
        new_member.save()
        return render(request, "videos.html", {'client': client, 'video': video})

    return render(request, "videos.html", {'client': client, 'video': video, 'category': category})


def join_nmb(request):
    cour = Cour.objects.filter(category="Les Nombres")
    video = Video.objects.filter(Video_Category="Les Nombres")
    category = "Les Nombres"
    client = Client.objects.filter(Q(email=user)).first()
    for x in cour:
        if x.client == client:
            return render(request, "videos.html", {'client': client, 'video': video, 'category': category})

    if request.method == 'POST':
        new_member = Cour(client=client, category="Les Nombres", Date=timezone.now())
        new_member.save()
        return render(request, "videos.html", {'client': client, 'video': video})

    return render(request, "videos.html", {'client': client, 'video': video, 'category': category})


def main(request):
    client = Client.objects.filter(email=user).first()
    users = Client.objects.all()
    return render(request, 'main.html', {'client': client, 'users': users})


def cls(request):
    users = Client.objects.all()
    client = Client.objects.filter(email=user).first()
    return render(request, "class.html", {'client': client, 'users': users})


def profile(request):
    client = Client.objects.filter(email=user).first()
    cour = Cour.objects.filter(client=client)
    return render(request, "profile.html", {'client': client, 'cour': cour})


def inscrire(request):
    client = Client.objects.all()
    return render(request, "login.html", {'client': client})


def sc(request):
    client = Client.objects.all()
    return render(request, "seconnecter.html", {'client': client})


def about(request):
    client = Client.objects.filter(email=user).first()
    return render(request, "about.html", {'client': client})


def contact(request):
    client = Client.objects.filter(email=user).first()
    return render(request, "contact.html", {'client': client})


def remarque(request):
    client = Client.objects.filter(email=user).first()
    return render(request, "remarque.html", {'client': client})


def cours(request):
    client = Client.objects.filter(email=user).first()
    cour = Cour.objects.filter(client=client)
    videos = Video.objects.all()
    return render(request, "cours.html", {'client': client, 'videos': videos, 'cour': cour})


def admin(request):
    return render(request, "admin", {})
