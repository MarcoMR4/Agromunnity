from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms

from .models import Cuadrilla, Productor, Trabajador, Huerta


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
    for a in c:
        productores.append([a.nombre, a.apellidoP])
    ElegirProductor = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=productores
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
        self.fields['ElegirProductor'].widget.attrs.update({'value': productor})

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
    #cargar productores desde la base de dtos 
    c = Productor.objects.order_by('apellidoP')
    productores =[]
    for a in c:
        productores.append([a.nombre, a.apellidoP])
    ElegirProductor = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=productores
    )

class ChangeCuadrilla(forms.Form):
    def __init__(self, *args, **kwargs):
        c = kwargs.pop('cuadrilla', None)
        cuadrilla = Cuadrilla.objects.get(id=c)
        nombre = cuadrilla.nombre
        gerente = cuadrilla.idGerenteCuadrilla
        capataz = cuadrilla.idCapatazCuadrilla
        super(ChangeCuadrilla, self).__init__(*args, **kwargs)
        self.fields['Nombre'].widget.attrs.update({'value': nombre})
        self.fields['ElegirGerente'].widget.attrs.update({'value': gerente})
        self.fields['ElegirCapataz'].widget.attrs.update({'value': capataz})

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    #cargar gerente desde la base de datos 
    g = Trabajador.objects.filter(rol='G_C')
    gerentes =[]
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
    for a in c:
        capataces.append([ a.Usuario.id, a.Usuario.username])
    ElegirCapataz = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=capataces
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