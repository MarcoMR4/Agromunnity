from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ChangeHuerta, UserLoginForm, AddEmplooye, AddTransport, AddCuadrilla, AddHuerta, AddProductor, AddMiembroCuadrilla, ChangeCuadrilla, AddPedido
from django.contrib.auth import authenticate, logout, login
from .models import Trabajador, User, Camion, Cuadrilla, Productor, Huerta, MiembroCuadrilla, Pedido
from django.contrib.auth.hashers import make_password

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
        ntrabajadores = Trabajador.objects.count()
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
                    'ntrabajadores': ntrabajadores,
                    "mensaje": request.session['Mensaje']
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, "user_enc_bit/worker.html", {
                    'form':form,
                    'trabajadores': trabajadores,
                    'ntrabajadores': ntrabajadores,
                    "error": request.session['Error']
                })
            else:
                return render(request, "user_enc_bit/worker.html", {
                    'form':form,
                    'trabajadores': trabajadores,
                    'ntrabajadores': ntrabajadores
                })
    else: 
        return render(request, 'denied.html')

@login_required
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

@login_required
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

@login_required
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
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('w')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

#Productor
@login_required
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

@login_required
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

@login_required
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

@login_required
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

#Cuadrillas
@login_required
def squad(request):
    if request.user.trabajador.rol == 'E_B':
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Cuadrilla'] = request.POST['Cuadrilla']
                    url = reverse('sd')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('s')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['Gerente'] = request.POST['ElegirGerente']
                    request.session['Capataz'] = request.POST['ElegirCapataz']
                    url = reverse('sr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('s')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Cuadrilla'] = request.POST['Cuadrilla']
                    url = reverse('sm')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('s')
                    return redirect(url)
        else:
            form = AddCuadrilla()
            cuadrillas = Cuadrilla.objects.all()
            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/squad.html', {
                    'form':form,
                    "mensaje": request.session['Mensaje'],
                    'cuadrillas': cuadrillas
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/squad.html', {
                    'form':form,
                    "error": request.session['Error'],
                    'cuadrillas': cuadrillas
                })
            else:
                return render(request, 'user_enc_bit/squad.html', {'form':form, 'cuadrillas': cuadrillas})
    else: 
        return render(request, 'denied.html')

@login_required
def squadDelete(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtiene el trabajador y elimina
            cuadrilla = request.session.get('Cuadrilla')
            c = Cuadrilla.objects.get(id=cuadrilla)
            c.delete()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Cuadrilla eliminada correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
            
        url = reverse('s')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def squadRegister(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se crea el usuario
            gerente=Trabajador.objects.get(Usuario_id=request.session.get('Gerente'))
            capataz=Trabajador.objects.get(Usuario_id=request.session.get('Capataz'))
            Cuadrilla.objects.create(
                nombre=request.session.get('Nombre'),
                idCapatazCuadrilla=capataz,
                idGerenteCuadrilla=gerente
            )
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen

            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Cuadrilla registrada correctamente."
        except Exception as e:
            print(e)
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
            
        url = reverse('s')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def squadModify(request):
    if request.user.trabajador.rol == 'E_B':
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Miembro'] = request.POST['Miembro']
                    url = reverse('smd')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    url = reverse('smr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['Gerente'] = request.POST['ElegirGerente']
                    request.session['Capataz'] = request.POST['ElegirCapataz']
                    url = reverse('sms')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='editar':
                try:
                    request.session['Miembro'] = request.POST['Miembro']
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    url = reverse('smm')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo guardar los datos, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
        else:

            c = request.session.get('Cuadrilla')
            formc = ChangeCuadrilla(cuadrilla=c)
            formm = AddMiembroCuadrilla()
            miembros = MiembroCuadrilla.objects.filter(idCuadrilla_id=c)

            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/squadModify.html', {
                    'formm':formm,
                    'formc':formc,
                    "mensaje": request.session['Mensaje'],
                    'miembros': miembros
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_bit/squadModify.html', {
                    'formm':formm,
                    'formc':formc,
                    "error": request.session['Error'],
                    'miembros': miembros
                })
            else:
                return render(request, 'user_enc_bit/squadModify.html', {
                    'formm':formm,
                    'formc':formc,
                    'miembros': miembros
                })
    else: 
        return render(request, 'denied.html')

@login_required
def squadMemberSave(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se modifican
            gerente=Trabajador.objects.get(Usuario_id=request.session.get('Gerente'))
            capataz=Trabajador.objects.get(Usuario_id=request.session.get('Capataz'))
            cuadrilla = Cuadrilla.objects.get(id=request.session.get('Cuadrilla'))
            cuadrilla.nombre=request.session.get('Nombre')
            cuadrilla.idCapatazCuadrilla=capataz
            cuadrilla.idGerenteCuadrilla=gerente
            cuadrilla.save()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Se guardaron los datos correctamente."
        except Exception as e:
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('sm')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def squadMemberDelete(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtiene el miembro y elimina
            miembro = request.session.get('Miembro')
            m = MiembroCuadrilla.objects.get(id=miembro)
            m.delete()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Miembro eliminado correctamente."
        except Exception as e:
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
            
        url = reverse('sm')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def squadMemberModify(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se modifican
            miembro = MiembroCuadrilla.objects.get(id=request.session.get('Miembro'))
            miembro.nombre=request.session.get('Nombre')
            miembro.apellidoP=request.session.get('AP')
            miembro.apellidoM=request.session.get('AM')
            miembro.save()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Se guardaron las modificaciones correctamente."
        except Exception as e:
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('sm')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def squadMemberRegister(request):
    if request.user.trabajador.rol == 'E_B':
        try:
            #Se obtienen los datos y se crea el miembro
            MiembroCuadrilla.objects.create(
                nombre=request.session.get('Nombre'),
                apellidoP=request.session.get('AP'),
                apellidoM=request.session.get('AM'),
                idCuadrilla_id=request.session.get('Cuadrilla')
            )
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen

            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Miembro registrado correctamente."
        except Exception as e:
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
            
        url = reverse('sm')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

#Encargado de transporte
@login_required
def transport(request):
    if request.user.trabajador.rol == 'E_T':
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Camion'] = request.POST['Camion']
                    url = reverse('td')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('t')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Chofer'] = request.POST['ElegirChofer']
                    request.session['Placa'] = request.POST['Placa']
                    request.session['Modelo'] = request.POST['Modelo']
                    request.session['Capacidad'] = 'Falta agregar'
                    print('estatus: ', request.POST['EstatusTransporte'])
                    request.session['Estatus'] = request.POST['EstatusTransporte']
                    url = reverse('tr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('t')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Camion'] = request.POST['Camion']
                    request.session['Chofer'] = request.POST['ElegirChofer']
                    request.session['Capacidad'] = request.POST['Capacidad']
                    request.session['Modelo'] = request.POST['Modelo']
                    print('estatus: ', request.POST['Estatus'])
                    request.session['Estatus'] = request.POST['Estatus']
                    url = reverse('tm')
                    return redirect(url)
                except Exception as e:
                    print(e)
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('t')
                    return redirect(url)
        else:

            form = AddTransport()
            camiones = Camion.objects.all()

            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_trans/transport.html', {
                    'form':form,
                    "mensaje": request.session['Mensaje'],
                    'camiones': camiones
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_trans/transport.html', {
                    'form':form,
                    "error": request.session['Error'],
                    'camiones': camiones
                })
            else:
                return render(request, 'user_enc_trans/transport.html', {
                    'form':form,
                    'camiones': camiones
                })
    else: 
        return render(request, 'denied.html')

@login_required
def transportDelete(request):
    if request.user.trabajador.rol == 'E_T':
        try:
            #Se obtiene el miembro y elimina
            camion = request.session.get('Camion')
            c = Camion.objects.get(id=camion)
            c.delete()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Vehiculo eliminado correctamente."
        except Exception as e:
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
            
        url = reverse('t')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def transportRegister(request):
    if request.user.trabajador.rol == 'E_T':
        try:
            #Se obtienen los datos y se crea el miembro
            Camion.objects.create(
                placa=request.session.get('Placa'),
                modelo=request.session.get('Modelo'),
                capacidad=request.session.get('Capacidad'),
                estatus=request.session.get('Estatus'),
                idChofer_id=request.session.get('Chofer')
            )
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen

            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Vehiculo registrado correctamente."
        except Exception as e:
            print(e)
            #se borra la sesion y toca volver a iniciar sesion
            #request.session.clear()
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
            
        url = reverse('t')
        return redirect(url)
    else: 
        return render(request, 'denied.html')

@login_required
def transportModify(request):
    if request.user.trabajador.rol == 'E_T':
        try:
            #Se obtienen los datos y se modifican
            camion = Camion.objects.get(id=request.session.get('Camion'))
            camion.idChofer_id =request.session.get('Chofer')
            camion.placa =request.session.get('Placa')
            camion.modelo =request.session.get('Modelo')
            camion.capacidad =request.session.get('Capacidad')
            camion.estatus =request.session.get('Estatus')
            camion.save()
            #Se guarda en memoria la operacion exitosa y redirige a la url de origen
            
            request.session['Operacion'] = 1
            request.session['Mensaje'] = "Se guardaron las modificaciones correctamente."
        except Exception as e:
            request.session['Operacion'] = 0
            request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
            
        url = reverse('t')
        return redirect(url)
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

@login_required
def order(request):
    if request.user.trabajador.rol == 'E_V':
        #si se envia un formulario
        if request.method == 'POST':
            if request.POST['Id']=='eliminar':
                try:
                    request.session['Miembro'] = request.POST['Miembro']
                    url = reverse('smd')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar la eliminación, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='agregar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    url = reverse('smr')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo realizar el registro, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='modificar':
                try:
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['Gerente'] = request.POST['ElegirGerente']
                    request.session['Capataz'] = request.POST['ElegirCapataz']
                    url = reverse('sms')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo modificar los datos, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
            elif request.POST['Id']=='editar':
                try:
                    request.session['Miembro'] = request.POST['Miembro']
                    request.session['Nombre'] = request.POST['Nombre']
                    request.session['AP'] = request.POST['AP']
                    request.session['AM'] = request.POST['AM']
                    url = reverse('smm')
                    return redirect(url)
                except Exception as e:
                    request.session['Operacion'] = 0
                    request.session['Error'] = "No se pudo guardar los datos, intente de nuevo."
                    url = reverse('sm')
                    return redirect(url)
        else:
            form = AddPedido()
            pedidos = Pedido.objects.all()
            if request.session.get('Operacion')==1:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_ventas/order.html', {
                    "mensaje": request.session['Mensaje'],
                    'form':form,
                    'pedidos': pedidos
                })
            elif request.session.get('Operacion')==0:
                request.session['Operacion'] = -1
                return render(request, 'user_enc_ventas/order.html', {
                    "error": request.session['Error'],
                    'form':form,
                    'pedidos': pedidos
                })
            else:
                return render(request, 'user_enc_ventas/order.html', {
                    'form':form,
                    'pedidos': pedidos
                })
    else: 
        return render(request, 'denied.html')