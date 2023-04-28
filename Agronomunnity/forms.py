from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms
from django.db.models.functions import Concat
from .models import Productor, Trabajador, RolTrabajador, Cliente, CamionTransporte, OrdenCorte, Cuadrilla


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

class AddWorker(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Correo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'placeholder':'Debe contener dominio @morelia.tecnm.mx'}
        )
    )

    Rol = forms.ModelChoiceField(
        queryset=RolTrabajador.objects.order_by('nomenclaturaRol'),
        empty_label="(Seleccione)", #Esto solo es el mensaje que sale al inicio de la lista que crea
        to_field_name="nombreRol", #Especifica que fila de la tabla o datos se usara
        widget=forms.Select( #Esto pone el estilo que teniamos antes pero vez que Claudio quiere que se note mas que son listas de seleccion
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    ) 

    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )


class AddTransport(forms.Form):

    Placa = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Capacidad = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Tipo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Candado = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Modelo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    estatusTransporte = (
    ('C_A', 'Activo'),
    ('C_I', 'Inactivo'),
    ('C_M', 'Mantenimiento')
    )

    Estatus = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusTransporte
    )

    Chofer = forms.ModelChoiceField(
        queryset = Trabajador.objects.filter(rol__nomenclaturaRol__exact='C_T'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddProducer(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class AddOrchard(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Fruta = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Ubicacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Localizacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Clave = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Inocuidad = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    estatusHuerta = (
    ('H_A', 'Activo'),
    ('H_I', 'Inactivo'),
    )

    Estatus = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusHuerta
    )

    Productor = forms.ModelChoiceField(
        queryset=Productor.objects.order_by('apellidoP'),
        empty_label="(Seleccione)",
        to_field_name="nombre",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddSquad(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    Ubicacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    estatusCuadrilla = (
    ('C_A', 'Activa'),
    ('C_I', 'Inactiva'),
    )

    Estatus = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusCuadrilla
    )

    Gerente = forms.ModelChoiceField(
        queryset = Trabajador.objects.filter(rol__nomenclaturaRol__exact='G_C'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    Jefe = forms.ModelChoiceField(
        queryset = Trabajador.objects.filter(rol__nomenclaturaRol__exact='J_C'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddSquadMember(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    noImss = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class AddOrder(forms.Form): 

    Numero = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'inputmode':'numeric'}
        )
    )

    Kilos = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'inputmode':'numeric'}
        )
    )

    Mercado = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )

    Destino = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )

    Cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.all().order_by('apellidoPCliente'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddClient(forms.Form): 

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    RFC = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class AddQuality(forms.Form): 

    Numero = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'inputmode':'numeric'}
        )
    )

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class AddCaliber(forms.Form): 

    Numero = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'inputmode':'numeric'}
        )
    )

class AddTrip(forms.Form): 

    Fecha = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    Salida = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required': 'true'}
        )
    )

    Llegada = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required': 'true'}
        )
    )

    Punto = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )

    estatusViaje = (
    ('V_P', 'No terminado'),
    ('V_T', 'Terminado'),
    )

    Estatus = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusViaje
    )

    Camion1 = forms.ModelChoiceField(
        queryset = CamionTransporte.objects.all().order_by('placaTransporte'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    Camion2 = forms.ModelChoiceField(
        queryset = CamionTransporte.objects.all().order_by('placaTransporte'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    Orden = forms.ModelChoiceField(
        queryset = OrdenCorte.objects.all().order_by('fechaOrden'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    Cuadrilla = forms.ModelChoiceField(
        queryset = Cuadrilla.objects.all().order_by('nombreCuadrilla'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )