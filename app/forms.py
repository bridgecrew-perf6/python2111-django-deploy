from django import forms
from django.db.models import fields
from app.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email',  'role','password']
        labels = {
            'name': 'Nombre',
            'email': 'Email',
            'role': 'Rol',
            'password': 'Contraseña',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(choices=User.OPCIONES_ROL, attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Contraseña',
        }
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
