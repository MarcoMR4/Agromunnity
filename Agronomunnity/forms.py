from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms

from .models import Trabajador


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={'id': 'username', 'name':'username', 'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'name':'password', 'class':'form-control'})
    )

class AddEmplooye(forms.Form):
#modificar datos en base al cambio de nombre de la base de datos
    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    Correo = forms.CharField(
        widget=forms.TextInput(
            attrs={'name':'correo', 'class': 'form-control col-sm-6', 'style': 'font-size: 12px;', 'placeholder':'Debe contener dominio @morelia.tecnm.mx'}
        )
    )
    users = Trabajador.tipoUsuario
    tU = list(users)
    tU.pop(0)
    Tipo = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=tU
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )


class AddTransport(forms.Form):

    Placa = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    Modelo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    estatusTransporte = (
    ('A', 'Activo'),
    ('I', 'Inactivo'),
    ('M', 'Mantenimiento')
    )
    EstatusTransporte = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=estatusTransporte
    )
    #cargar choferes desde la base de dtos 
    choferes = (
    ('1', 'chofer1'),
    ('2', 'chofer2'),
    ('3', 'chofer3')
    )
    ElegirChofer = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=choferes
    )

#Formularios faltantes:
#Agregar huerta, agregar productor de huerta, agregar cuadrilla, agregar miembro cuadrilla

class AddProductor(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )

class AddHuerta(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    ubicacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    fruta = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    estatusHuerta = (
    ('H_A', 'Activo'),
    ('H_I', 'Inactivo'),
    )
    EstatusHuerta = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=estatusHuerta
    )
    #cargar productores desde la base de dtos 
    productores = (
    ('1', 'productor1'),
    ('2', 'productor2'),
    ('3', 'productor3')
    )
    ElegirProductor = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=productores
    )

class AddCuadrilla(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    #cargar gerente desde la base de datos 
    gerente = (
    ('1', 'gerente1'),
    ('2', 'gerente2'),
    ('3', 'gerente3')
    )
    ElegirGerente = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=gerente
    )
    #cargar capataz desde la base de datos 
    capataz = (
    ('1', 'capataz1'),
    ('2', 'capataz2'),
    ('3', 'capataz3')
    )
    ElegirCapataz = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=capataz
    )

class AddMiembroCuadrilla(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    #cargar cuadrilla desde la base de datos 
    cuadrilla = (
    ('1', 'cuadrilla1'),
    ('2', 'cuadrilla2'),
    ('3', 'cuadrilla3')
    )
    ElegirCuadrilla = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=cuadrilla
    )
