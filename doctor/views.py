from django.shortcuts import render, redirect
from doctor.forms import DoctorForm
from django.contrib import messages
from doctor.models import Doctor

def index(request):
    context = {
        'doctores': Doctor.objects.all()
    }
    return render(request, 'index.html', context)


def add(request):

    if request.method == 'POST':

        form = DoctorForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, "Doctor creado correctamente")
                return redirect('/doctor')
        else:
            messages.error(request, "Formulario procesado con errroes.")
            return render(request, 'doctor/add.html', {'form': form})

    else:
        context = {
            'form': DoctorForm()
        }
        return render(request, 'add.html', context)


def edit(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor editado correctamente")
            return redirect('/doctor')
        else:
            messages.error(request, "Formulario procesado con errroes.")
            return render(request, 'doctor/edit.html', {'form': form, 'doctor': doctor})
    else:
        form = DoctorForm(instance=doctor)
        return render(request, 'edit.html', {'form': form, 'doctor': doctor})
        

def delete(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    messages.success(request, "Doctor eliminado correctamente")
    return redirect('/doctor')
