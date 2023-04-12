from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ChangeHuerta, ChangeProductor, UserLoginForm, AddEmplooye, AddTransport, AddCuadrilla, AddHuerta, AddProductor, AddMiembroCuadrilla, ChangeCuadrilla
from django.contrib.auth import authenticate, logout, login
from django.template import RequestContext
from .models import Trabajador, User, Camion, Cuadrilla, Productor, Huerta, MiembroCuadrilla
from django.contrib.auth.hashers import make_password
from django.core.cache import cache

#dashboard 
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
#Encargado de bitacora
#Trabajador
@login_required
def worker(request):
    if request.user.trabajador.rol == 'E_B':
        #Consultas necesarias para mostrar en plantilla
        form = AddEmplooye()
        trabajadores = Trabajador.objects.all()
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Trabajador'] = request.POST['Trabajador']
                    url = reverse('wd')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('w')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Nombres'] = request.POST['Nombre']
                    request.session['Apellidos'] = request.POST['AP']+' '+request.POST['AM']
                    request.session['Telefono'] = request.POST['Telefono']
                    request.session['Correo'] = request.POST['Correo']
                    request.session['Rol'] = request.POST['Tipo']
                    url = reverse('wr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('w')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Trabajador'] = request.POST['Trabajador']
                    request.session['Nombres'] = request.POST['Nombre']
                    print(request.POST['Correo'])
                    request.session['Apellidos'] = request.POST['Apellidos']
                    request.session['Telefono'] = request.POST['Telefono']
                    request.session['Correo'] = request.POST['Correo']
                    request.session['Rol'] = request.POST['Tipo']
                    url = reverse('wm')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('w')
                    return redirect(url)
        else:
            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, "user_enc_bit/worker.html", {
                    'form':form,
                    'trabajadores': trabajadores,
                    "mensaje": request.session['Mensaje']
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, "user_enc_bit/worker.html", {
                    'form':form,
                    'trabajadores': trabajadores,
                    "error": request.session['Error']
                })
            else:
                return render(request, "user_enc_bit/worker.html", {'form':form, 'trabajadores': trabajadores})
    else: 
        return render(request, 'denied.html')

def workerDelete(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtiene el trabajador y elimina
            trabajador = request.session.get('Trabajador')
            t = Trabajador.objects.get(id=trabajador)
            u = User.objects.get(id = t.Usuario_id)
            u.delete() 
            t.delete()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Trabajador eliminado correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
            
        url = reverse('w')
        return redirect(url)
    else: 
        return render(request, 'denied.html')
    
def workerRegister(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se crea el usuario
            usuario = User.objects.create(
                username=request.session.get('Nombres'),
                last_name=request.session.get('Apellidos'),
                password= make_password(request.session.get('Telefono'))
            )
        
            Trabajador.objects.create(
                telefono=request.session.get('Telefono'),
                correoPersonal=request.session.get('Correo'),
                rol=request.session.get('Rol'),
                Usuario_id=usuario.id
            )
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen

            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Trabajador registrado correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
            
        url = reverse('w')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

def workerModify(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se modifican
            trabajador = Trabajador.objects.get(id=request.session.get('Trabajador'))
            usuario = User.objects.get(id=trabajador.Usuario_id)

            usuario.username=request.session.get('Nombres')
            usuario.last_name=request.session.get('Apellidos')
            usuario.save()
            trabajador.telefono=request.session.get('Telefono')
            trabajador.correoPersonal=request.session.get('Correo')
            trabajador.rol=request.session.get('Rol')
            trabajador.save()

            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Se guardaron las modificaciones correctamente."
        except Exception as e:
            print(e)
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('w')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

#Productor
def producer(request):
    if request.user.trabajador.rol == 'E_B':
        #Consultas necesarias para mostrar en plantilla
        form = AddProductor()
        productores = Productor.objects.all()
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Productor'] = request.POST['Productor']
                    url = reverse('pd')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('p')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    request.session['Telefono'] = request.POST['Telefono']
                    url = reverse('pr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('p')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Productor'] = request.POST['Productor']
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    request.session['Telefono'] = request.POST['Telefono']
                    url = reverse('pm')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('p')
                    return redirect(url)
        else:
            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/producer.html', {
                    'form':form,
                    "mensaje": request.session['Mensaje'],
                    'productores': productores
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/producer.html', {
                    'form':form,
                    "error": request.session['Error'],
                    'productores': productores
                })
            else:
                return render(request, "user_enc_bit/producer.html", {'form':form, 'productores': productores})
    else: 
        return render(request, 'denied.html')

def producerRegister(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se crea el usuario
            Productor.objects.create(
                nombre=request.session.get('Nombre'),
                apellidoP=request.session.get('AP'),
                apellidoM=request.session.get('AM'),
                telefono=request.session.get('Telefono'),
            )
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen

            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Productor registrado correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
            
        url = reverse('p')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

def producerDelete(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtiene el trabajador y elimina
            productor = request.session.get('Productor')
            p = Productor.objects.get(id=productor)
            p.delete()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Productor eliminado correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
            
        url = reverse('p')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

def producerModify(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se modifican
            productor = Productor.objects.get(id=request.session.get('Productor'))
            productor.nombre=request.session.get('Nombre')
            productor.apellidoP=request.session.get('AP')
            productor.apellidoM=request.session.get('AM')
            productor.telefono=request.session.get('Telefono')
            productor.save()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Se guardaron las modificaciones correctamente."
        except Exception as e:
            print(e)
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('p')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def transportRegister(request):
    if request.user.trabajador.rol == 'E_B':
        form = AddTransport()
        camiones = Camion.objects.all()
        if request.method == 'POST':
            try:
                chofer=Trabajador.objects.get(Usuario_id=request.POST['ElegirChofer'])
                camion = Camion.objects.create(
                    placa=request.POST['Placa'],
                    modelo=request.POST['Modelo'],
                    capacidad='8',
                    estatus=request.POST['EstatusTransporte'],
                    idChofer=chofer
                )
                return render(request, 'user_enc_bit/transportRegister.html', {
                    'form':form,
                    "mensaje": "Camión Registrado exitosamente",
                    'camiones': camiones})
            except Exception as e:
                print(e)
                return render(request, 'user_enc_bit/transportRegister.html', {
                    'form':form,
                    "error": e,
                    'camiones': camiones})
        else:
            return render(request, 'user_enc_bit/transportRegister.html', {'form':form, 'camiones': camiones})
    else: 
        return render(request, 'denied.html')
    
def squadRegister(request):
    if request.user.trabajador.rol == 'E_B':
        form = AddCuadrilla()
        cuadrillas = Cuadrilla.objects.all()
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    c = Cuadrilla.objects.get(id=request.POST['Cuadrilla']) 
                    c.delete()
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'form':form,
                        "mensaje": "Cuadrilla eliminada correctamente.",
                        'cuadrillas': cuadrillas})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'form':form,
                        "error": "No se pudo realizar la eliminación, intente de nuevo.",
                        'cuadrillas': cuadrillas})
            elif request.POST['Id']=='agregar':
                try:
                    gerente=Trabajador.objects.get(Usuario_id=request.POST['ElegirGerente'])
                    capataz=Trabajador.objects.get(Usuario_id=request.POST['ElegirCapataz'])
                    Cuadrilla.objects.create(
                        nombre=request.POST['Nombre'],
                        idCapatazCuadrilla=capataz,
                        idGerenteCuadrilla=gerente
                    )
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'form':form,
                        "mensaje": "Cuadrilla registrada correctamente.",
                        'cuadrillas': cuadrillas})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'form':form,
                        "error": 'No se pudo realizar el registro, intente de nuevo.',
                        'cuadrillas': cuadrillas})
            elif request.POST['Id']=='modificar':
                try:
                    cuadrilla=request.POST['Cuadrilla']
                    request.session['cuadrilla'] = cuadrilla
                    url = reverse('sm')
                    return redirect(url)
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'form':form,
                        "error": "A ocurrido un error, intente de nuevo.",
                        'cuadrillas': cuadrillas})
        else:
            return render(request, 'user_enc_bit/squadRegister.html', {'form':form, 'cuadrillas': cuadrillas})
    else: 
        return render(request, 'denied.html')

def squadModify(request):
    if request.user.trabajador.rol == 'E_B':
        c = request.session.get('cuadrilla')
        formc = ChangeCuadrilla(cuadrilla=c)
        formm = AddMiembroCuadrilla()
        miembros = MiembroCuadrilla.objects.filter(idCuadrilla_id=c)
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    m = MiembroCuadrilla.objects.get(id=request.POST['Miembro']) 
                    m.delete()
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formm':formm,
                        'formc':formc,
                        "mensaje": "Se elimino el miembro correctamente.",
                        'miembros': miembros})
                except Exception as e:
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formm':formm,
                        'formc':formc,
                        "error": "No se pudo realizar la eliminación, intente de nuevo.",
                        'miembros': miembros})
            elif request.POST['Id']=='agregar':
                try:
                    MiembroCuadrilla.objects.create(
                        nombre=request.POST['Nombre'],
                        apellidoP=request.POST['AP'],
                        apellidoM=request.POST['AM'],
                        idCuadrilla_id=c
                    )
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formc':formc,
                        'formm':formm,
                        "mensaje": "Miembro Registrado correctamente.",
                        'miembros': miembros})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formc':formc,
                        'formm':formm,
                        "error": "No se pudo realizar el registro, intente de nuevo.",
                        'miembros': miembros})
            elif request.POST['Id']=='modificar':
                try:
                    gerente=Trabajador.objects.get(Usuario_id=request.POST['ElegirGerente'])
                    capataz=Trabajador.objects.get(Usuario_id=request.POST['ElegirCapataz'])
                    cuadrilla = Cuadrilla.objects.get(id = c)
                    cuadrilla.nombre = request.POST['Nombre']
                    cuadrilla.idCapatazCuadrilla = capataz
                    cuadrilla.idGerenteCuadrilla = gerente
                    cuadrilla.save()
                    formc = ChangeCuadrilla(cuadrilla=c)
                    cuadrillas = Cuadrilla.objects.all()
                    return render(request, 'user_enc_bit/squadRegister.html', {
                        'formc':formc,
                        'formm':formm,
                        "mensaje": "Se guardaron las modificaciones correctamente.",
                        'cuadrillas': cuadrillas})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formc':formc,
                        'formm':formm,
                        "error": "No se pudo modificar los datos, intente de nuevo.",
                        'miembros': miembros})
            elif request.POST['Id']=='editar':
                try:
                    miembro = MiembroCuadrilla.objects.get(id=request.POST['Miembro'])
                    miembro.nombre = request.POST['Nombre']
                    miembro.apellidoP = request.POST['AP']
                    miembro.apellidoM = request.POST['AM']
                    miembro.save()
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formc':formc,
                        'formm':formm,
                        "mensaje": "Se guardaron las modificaciones correctamente.",
                        'miembros': miembros})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/squadModify.html', {
                        'formc':formc,
                        'formm':formm,
                        "error": "No se pudo realizar la modificación, intente de nuevo.",
                        'miembros': miembros})
        else:
            return render(request, 'user_enc_bit/squadModify.html', {
                'formc':formc,
                'formm':formm,
                'miembros': miembros})
    else: 
        return render(request, 'denied.html')

def orchardRegister(request):
    if request.user.trabajador.rol == 'E_B':
        form = AddHuerta()
        huertas = Huerta.objects.all()
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    c = Huerta.objects.get(id=request.POST['Huerta']) 
                    c.delete()
                    return render(request, 'user_enc_bit/orchardRegister.html', {
                        'form':form,
                        "mensaje": "Se elimino la huerta correctamente.",
                        'huertas': huertas})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/orchardRegister.html', {
                        'form':form,
                        "error": "No se pudo eliminar la huerta, intente de nuevo.",
                        'huertas': huertas})
            elif request.POST['Id']=='agregar':
                try:
                    productor=Productor.objects.get(nombre=request.POST['ElegirProductor'])
                    Huerta.objects.create(
                        nombre=request.POST['nombre'],
                        ubicacion=request.POST['ubicacion'],
                        fruta=request.POST['fruta'],
                        estatus=request.POST['EstatusHuerta'],
                        idProductor=productor
                    )
                    return render(request, 'user_enc_bit/orchardRegister.html', {
                        'form':form,
                        "mensaje": "Huerta registrada correctamente.",
                        'huertas': huertas})
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/orchardRegister.html', {
                        'form':form,
                        "error": "No se pudo registrar la huerta, intente de nuevo.",
                        'huertas': huertas})
            elif request.POST['Id']=='modificar':
                try:
                    huerta=request.POST['Huerta']
                    request.session['huerta'] = huerta
                    url = reverse('om')
                    return redirect(url)
                except Exception as e:
                    print(e)
                    return render(request, 'user_enc_bit/orchardRegister.html', {
                        'form':form,
                        "error": "A ocurrido un error, intente de nuevo.",
                        'huertas': huertas})

        else:
            return render(request, 'user_enc_bit/orchardRegister.html', {'form':form, 'huertas': huertas})
    else: 
        return render(request, 'denied.html')
    
def orchardModify(request):
    if request.user.trabajador.rol == 'E_B':
        c = request.session.get('huerta')
        formc = ChangeHuerta(huerta=c)
        formm = AddHuerta()
        origen = Huerta.objects.all()
        huertas = Huerta.objects.filter(id=c)
        
        if request.method == 'POST':
            try:
                productor=Productor.objects.get(nombre=request.POST['ElegirProductor'])
                huerta = Huerta.objects.get(id = c)
                huerta.nombre = request.POST['Nombre']
                huerta.ubicacion = request.POST['Ubicacion']
                huerta.fruta = request.POST['Fruta']
                huerta.estatus = request.POST['EstatusHuerta']
                huerta.idProductor = productor
                huerta.save()
                formc = ChangeHuerta(huerta=c)
                url = reverse('or')
                return redirect(url)
            except Exception as e:
                print(e)
                return render(request, 'user_enc_bit/orchardRegister.html', {
                    'formc':formc,
                    'formm':formm,
                    "error": "No se pudo modificar los datos, intente de nuevo.",
                    'huertas': huertas})
        else:
            return render(request, 'user_enc_bit/orchardModify.html', {
                'formc':formc,
                'formm':formm,
                'huertas': origen})
    else: 
        return render(request, 'denied.html')