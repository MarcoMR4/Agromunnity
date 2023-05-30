from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.db.models import Min, Max
from django import forms
from django.db.models.functions import Concat
from .models import Productor, Trabajador, Huerta, Pedido, RolTrabajador, Cliente, CamionTransporte, OrdenCorte, Cuadrilla, Calibre, Calidad, PrecioAutorizado, ViajeCorte


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
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    Correo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
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
        ('','(Seleccione)'),
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
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'required':'true', 'style': 'font-size: 12px;'}
        )
    )

class AddOrchard(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;','required':'true'}
        )
    )

    fruta = (
        ('','(Seleccione)'),
        ('AGT', 'Aguacate'),
    )
    Fruta = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        ),
        choices=fruta
    )

    municipio = (
        ('','(Seleccione)'),
        ('UPN','Uruapan'),
        ('SES','Salvador Escalante'),
        ('TAN','Tancítaro'),
        ('PER','Peribán'),
        ('TCM','Tacámbaro'),
        ('ADR','Ario de Rosales')
    )
    Ubicacion = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        ),
        choices=municipio
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
    ('','(Seleccione)'),
    ('H_D', 'Con fruta Disponible'),
    ('H_S', 'Sin fruta disponible')
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
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    Ubicacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        )
    )

    estatusCuadrilla = (
    ('', '(Seleccione)'),
    ('C_L', 'Libre'),
    ('C_O', 'Ocupada'),
    )

    Estatus = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
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

    mercadoPedido = (
        ('', '(Seleccione)'),
        ('M_N', 'Nacional'),
        ('M_E', 'Exportación'),
        ('M_O', 'Otros destinos'),
    )

    Mercado = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=mercadoPedido
    )

    Observacion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    DatosT = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'hidden': 'true'}
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

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
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
        queryset = Cuadrilla.objects.filter(estatusCuadrilla='C_L').order_by('nombreCuadrilla'),
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
        ('','(Seleccione)'),
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

    Huerta = forms.ModelChoiceField(
        queryset = Huerta.objects.all().order_by('nombreHuerta'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

    corte = (
        ('','(Seleccione)'),
        ('AVN', 'Aventajado'),
        ('FLC', 'Flor loca'),
    )
    Corte = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true'}
        ),
        choices=corte
    )

    Pedido = forms.ModelChoiceField(
        queryset = Pedido.objects.filter(estatusPedido='P_I'),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddPrice(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pcr = PrecioAutorizado.objects.values_list('estadoAplica', flat=True).distinct()
        psr = [estado for estado in self.estados if estado[0] not in pcr]
        self.fields['Estado'].choices = psr

    Fijo = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        )
    )

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Actual = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        )
    )

    Vigencia = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required':'true', 'type': 'date'}
        )
    )

    estados = (
        ('','(Seleccione)'),
        ('AGS', 'Aguascalientes'),
        ('BC', 'Baja California'),
        ('BCS', 'Baja California Sur'),
        ('CAM', 'Campeche'),
        ('CHIS', 'Chiapas'),
        ('CHIH', 'Chihuahua'),
        ('CDMX', 'Ciudad de México'),
        ('COAH', 'Coahuila'),
        ('COL', 'Colima'),
        ('DGO', 'Durango'),
        ('GTO', 'Guanajuato'),
        ('GRO', 'Guerrero'),
        ('HGO', 'Hidalgo'),
        ('JAL', 'Jalisco'),
        ('MEX', 'México'),
        ('MIC', 'Michoacán'),
        ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'),
        ('NL', 'Nuevo León'),
        ('OAX', 'Oaxaca'),
        ('PUE', 'Puebla'),
        ('QRO', 'Querétaro'),
        ('QR', 'Quintana Roo'),
        ('SLP', 'San Luis Potosí'),
        ('SIN', 'Sinaloa'),
        ('SON', 'Sonora'),
        ('TAB', 'Tabasco'),
        ('TAMPS', 'Tamaulipas'),
        ('TLAX', 'Tlaxcala'),
        ('VER', 'Veracruz'),
        ('YUC', 'Yucatán'),
        ('ZAC', 'Zacatecas'),
    )

    Estado = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        ),
        choices=estados
    )

class AddFruit(forms.Form):

    Descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

    Precio = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        )
    )

    Huerta = forms.ModelChoiceField(
        queryset = Huerta.objects.exclude(frutahuerta__isnull=False),
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'} 
        )
    )

class AddRol(forms.Form):

    Nomenclatura = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'},
        ),
        max_length=3,
    )


    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class AddReport(forms.Form):
    Viaje = forms.ModelChoiceField(
        queryset=ViajeCorte.objects.none(),  # Inicialmente se establece como una consulta vacía
        empty_label="(Seleccione)",
        widget=forms.Select(
            attrs={'class': 'form-control', 'required':'true', 'style': 'font-size: 12px;'}
        )
    )

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtén el valor del atributo 'request' si está presente
        super().__init__(*args, **kwargs)
        if request:
            self.fields['Viaje'].queryset = ViajeCorte.objects.filter(idCuadrilla__idJefeCuadrilla=request.user.trabajador.id).exclude(reportecorte__idViaje__isnull=False)
 

    Cajas = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'inputmode':'numeric'}
        )
    )

    Observaciones = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;'}
        )
    )

class SearchTrip(forms.Form):
    
    fecha_inicio = ViajeCorte.objects.all().aggregate(Min('fechaViaje')).get('fechaViaje__min')
    fecha_fin = ViajeCorte.objects.all().aggregate(Max('fechaViaje')).get('fechaViaje__max')

    Inicio = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required': True, 'type': 'date', 'value': fecha_inicio}
        )
    )
    Fin = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'style': 'font-size: 12px;', 'required': True, 'type': 'date', 'value': fecha_fin}
        )
    )