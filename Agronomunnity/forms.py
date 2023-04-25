from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms
from django.db.models.functions import Concat
from .models import Cuadrilla, Productor, Trabajador, Huerta, RolTrabajador


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

class ChangeProductor(forms.Form):
    def __init__(self, *args, **kwargs):
        c = kwargs.pop('productor', None)
        productor = Productor.objects.get(id=c)
        nombre = productor.nombre
        ap = productor.apellidoP
        am = productor.apellidoM
        telefono = productor.telefono
        super(ChangeProductor, self).__init__(*args, **kwargs)
        self.fields['Nombre'].widget.attrs.update({'value': nombre})
        self.fields['AP'].widget.attrs.update({'value': ap})
        self.fields['AM'].widget.attrs.update({'value': am})
        self.fields['Telefono'].widget.attrs.update({'value': telefono})

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


class ChangeHuerta(forms.Form):
    def __init__(self, *args, **kwargs):
        c = kwargs.pop('huerta', None)
        huerta = Huerta.objects.get(id=c)
        nombre = huerta.nombre
        ubicacion = huerta.ubicacion
        fruta = huerta.fruta
        estatus = huerta.estatus
        productor = huerta.idProductor
        super(ChangeHuerta, self).__init__(*args, **kwargs)
        self.fields['Nombre'].widget.attrs.update({'value': nombre})
        self.fields['Ubicacion'].widget.attrs.update({'value': ubicacion})
        self.fields['Fruta'].widget.attrs.update({'value': fruta})
        self.fields['EstatusHuerta'].widget.attrs.update({'value': estatus})

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
    Fruta = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    estatusHuerta = (
    ('H_A', 'Activo'),
    ('H_I', 'Inactivo'),
    )
    EstatusHuerta = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusHuerta
    )

    ElegirProductor = forms.ModelChoiceField(
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

class AddPedido(forms.Form): 

    numeroPedido = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    nombreCliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    aPCliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    aMCliente = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    avance = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )
    mercado = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )
    destino = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
    )