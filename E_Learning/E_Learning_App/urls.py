from . import views
from django.urls import path

app_name = 'E_Learning_App'

urlpatterns = [

    # URLS basés sur les Templates
    path('', views.sc, name="sc"),
    path('se_connecter', views.sc, name="sc"),
    path('inscrire', views.inscrire, name="inscrire"),
    path('main', views.main, name="main"),
    path('class', views.cls, name="cls"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('remarque', views.remarque, name="remarque"),
    path('profile', views.profile, name="profile"),
    path('cours', views.cours, name="cours"),

    # URLS basés sur les Modèles
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('remarque/', views.msg, name="msg"),
    path('class/Interactive', views.join_int, name="join_int"),
    path('class/Alphabet', views.join_alp, name="join_alp"),
    path('class/Numbers', views.join_nmb, name="join_nmb"),

]
