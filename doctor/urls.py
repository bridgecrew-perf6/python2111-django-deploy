from django.urls import path
from . import views

# localhost:8000/doctor/

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
]
