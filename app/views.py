from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import UserForm, LoginForm
from app.models import User
import bcrypt

def index(request):
    
    if 'usuario' not in request.session:
        return redirect('/login')
  
    return render(request, 'app/index.html')


def contacto(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    
    if User.ADMINISTRADOR != request.session['usuario']['role']:
        messages.error(request,"No tienes permisos para entrar a ADMINISTRADOR")
        return redirect('/')
    
    return render(request, 'app/contacto.html')

def vision(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    return render(request, 'app/vision.html')


def mision(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    return render(request, 'app/mision.html')


def prueba_mensajes(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    messages.error(request, "Prueba de Mensaje - error")
    messages.success(request, "Prueba de Mensaje - success")
    messages.info(request, "Prueba de Mensaje - info")
    messages.warning(request, "Prueba de Mensaje - warning")
    
    return redirect('/')



def register(request):
    
    if 'usuario' in request.session:
        return redirect('/')
    
    
    if request.method == 'POST':
        #POST
        
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()            
            messages.success(request, "Usuario creado correctamente")
            return redirect('/')
        else:
            messages.error(request, "Formulario procesado con errroes.")
            return render(request, 'app/register.html', {'form':form})
    else:
        # GET
        context = {
            'form' : UserForm()
        }
        
        return render(request, 'app/register.html', context)
    
def login(request):
    
    if 'usuario' in request.session:
        return redirect('/')
    
    if request.method == 'POST':
        # POST
        user = User.objects.filter(email=request.POST['email'])
        
        if user:
            usuario_login = user[0]
            
            if bcrypt.checkpw(request.POST['password'].encode(),  usuario_login.password.encode()):
                print("USUARIO CORRECTO")
                request.session['usuario'] = { 'nombre':usuario_login.name , 'email':usuario_login.email,'role':usuario_login.role, 'role_nombre':usuario_login.get_role_display(), 'id':usuario_login.id}
                return redirect('/')
            else:
                print("USUARIO NO ES SU CONTRASEÑA")
                messages.error(request, "USUARIO NO ES SU CONTRASEÑA")

        else:
            messages.error(request, "Usuario no encontrado")
        
        return redirect('/login')
            
        
        
    else:
        
        # GET
        context = {
            'form' : LoginForm()
        }
            
        return render(request, 'app/login.html', context)
    
    
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
        
    return redirect('/')