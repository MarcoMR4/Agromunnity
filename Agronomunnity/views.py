from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, AddEmplooye, AddTransport
from django.contrib.auth import authenticate, logout, login
from django.template import RequestContext
from .models import Trabajador, User
from django.contrib.auth.hashers import make_password

@login_required
def index(request):
    return render(request, 'index.html')

def li(request):
    if request.method == 'GET':
        return render(request, "login.html",{
            "form": UserLoginForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "login.html",{
                "form": UserLoginForm,
                "error": "Usuario o contraseña incorrectos."
            })
        else:
            login(request, user)
            return redirect('index')

def lo(request):
    logout(request)
    return redirect('login')
#modificar nombre de datos en base a los cambios de nombre en las bases de datos
@login_required
def workerRegister(request):
    if request.user.user.tipouser == 'E_B':
        form = AddEmplooye()
        if request.method == 'POST':
            try:
                nombre = request.POST['Nombre']
                contrasenia = 'Agro-'+request.POST['Telefono']
                usuario = User.objects.create(
                    username=nombre,
                    password= make_password(contrasenia)
                )
                trabajador = user.objects.create(
                    telefono=request.POST['Telefono'],
                    correoPersonal=request.POST['Correo'],
                    tipouser=request.POST['Tipo'],
                    user_id=usuario.id
                )
                return render(request, "user_enc_bit/workerRegister.html", {
                    'form':form,
                    "mensaje": "Trabajador Registrado exitosamente"})
            except Exception as e:
                print(e)
                return render(request, "user_enc_bit/workerRegister.html", {
                    'form':form,
                    "error": e})
        else:
            return render(request, "user_enc_bit/workerRegister.html", {'form':form})
    else: 
        return render(request, 'denied.html')
    
@login_required
def transportRegister(request):
    if request.user.user.tipouser == 'E_B':
        form = AddTransport()

    return render(request, 'user_enc_bit/transportRegister.html', 
                     {'form':form})