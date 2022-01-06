from django import forms
from doctor.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'detalle', 'profesion']
        labels = {
            'nombre': 'Nombre',
            'detalle': 'Detalle',
            'profesion': 'Profesión',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
        }