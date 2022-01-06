from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('contacto', views.contacto),
    path('vision', views.vision),
    path('mision', views.mision),
    path('prueba', views.prueba_mensajes),
    
    path('login', views.login),
    path('register', views.register),
    
    path('logout', views.logout),
    
]
