from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms

from .models import Cuadrilla, Productor, Trabajador


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
    users = Trabajador.tipoUsuario
    tU = list(users)
    Tipo = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=tU
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
    Modelo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    estatusTransporte = (
    ('A', 'Activo'),
    ('I', 'Inactivo'),
    ('M', 'Mantenimiento')
    )
    EstatusTransporte = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estatusTransporte
    )
    #cargar choferes desde la base de dtos 
    c = Trabajador.objects.filter(rol='C_T')
    choferes =[]
    c = Trabajador.objects.filter(rol='C_T')
    for a in c:
        choferes.append([ a.Usuario.id, a.Usuario.username])
    ElegirChofer = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=choferes
    )

class AddProductor(forms.Form):

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

class AddHuerta(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    ubicacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    fruta = forms.CharField(
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
    #cargar productores desde la base de dtos 
    c = Productor.objects.order_by('apellidoP')
    productores =[]
    c = Productor.objects.order_by('apellidoP')
    for a in c:
        productores.append([a.nombre, a.apellidoP])
    ElegirProductor = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=productores
    )

class AddCuadrilla(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    #cargar gerente desde la base de datos 
    g = Trabajador.objects.filter(rol='G_C')
    gerentes =[]
    g = Trabajador.objects.filter(rol='G_C')
    for a in g:
        gerentes.append([ a.Usuario.id, a.Usuario.username])
    ElegirGerente = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=gerentes
    )
    #cargar capataz desde la base de datos 
    c = Trabajador.objects.filter(rol='C_C')
    capataces =[]
    c = Trabajador.objects.filter(rol='C_C')
    for a in c:
        capataces.append([ a.Usuario.id, a.Usuario.username])
    ElegirCapataz = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=capataces
    )

class AddMiembroCuadrilla(forms.Form):

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
    #cargar cuadrilla desde la base de datos 
    c = Cuadrilla.objects.order_by('nombre')
    cuadrillas =[]
    c = Cuadrilla.objects.order_by('nombre')
    for a in c:
        cuadrillas.append([ a.Usuario.id, a.Usuario.username])
    ElegirChofer = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=cuadrillas
    )