from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms
from django.db.models.functions import Concat
from .models import Productor, Trabajador, Huerta, Pedido, RolTrabajador, Cliente, CamionTransporte, OrdenCorte, Cuadrilla, Calibre, Calidad


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
            attrs={'class': 'form-control', 'required':'true', 'style': 'font-size: 12px;'} 
        )
    ) 

    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    def clean_Telefono(self):
        cleaned_data = super().clean()
        telefono=self.cleaned_data['Telefono']
        if not telefono.isdigit():
            raise forms.ValidationError('El número de teléfono debe contener solo digitos')
        if len(telefono) != 10:
            raise forms.ValidationError('El número de teléfono debe tener solo 10 digitos')
        return telefono

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
    def clean(self, *args, **kwargs):
        cleaned_data = super(AddProducer, self).clean(*args, **kwargs)
        telefono = cleaned_data.get('Telefono', None)
        if telefono is not None:
            if len(telefono) != 10:
                self.add_error('telefono', 'El número de teléfono debe tener solo 10 digitos')

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
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        )
    )

    Tkilos = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric', 'readonly':''}
        ),
        required=False,
        initial=None
    )



    Kilos = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        ),
        required=False
    )

    Mercado = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Destino = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.all().order_by('apellidoPCliente'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    Calidad = forms.ModelChoiceField(
        queryset = Calidad.objects.all(),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        ),
        required=False,
    )

    Calibre = forms.ModelChoiceField(
        queryset = Calibre.objects.all(),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        ),
        required=False,
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

    Salida = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required': 'true', 'type': 'time'}
        )
    )


    Punto = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false'}
        )
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
        queryset = OrdenCorte.objects.all().filter(idPedido__estatusPedido='P_O'),
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

    Huerta = forms.ModelChoiceField(
        queryset = Huerta.objects.all().order_by('nombreHuerta'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddIncident(forms.Form):

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'false', 'rows': '3'}
        )
    )

    Fecha = forms.DateField(
        
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'type': 'date'}
        )
    )

    temas = (
        ('B_T','Bitacoras'),
        ('C_M','Camiones'),
        ('C_A','Calidad'),
        ('C_L','Clientes'),
        ('C_D','Cuadrillas'),
        ('D_C','Documentos'),
        ('E_N','Encargados'),
        ('G_R','Gerentes'),
        ('H_R','Huertas'),
        ('G_F','Jefes'),
        ('O_C','Ordenes de corte'),
        ('P_D','Pedidos'),
        ('P_T','Productores'),
        ('T_B','Trabajadores'),
        ('T_P','Transportes'),
        ('V_J','Viajes'),
    )

    Tema = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=temas
    )

class AddCourtOrder(forms.Form):

    Fruta = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Corte = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Pedido = forms.ModelChoiceField(
        queryset = Pedido.objects.filter(estatusPedido='P_I'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )