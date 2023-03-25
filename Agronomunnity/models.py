from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Trabajador(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10, blank = True)
    correoPersonal = models.EmailField(max_length = 254, blank = True)
    tipoUsuario = (
        ('E_B', 'Encargado de bitacora'),
        ('E_V', 'Encargado de ventas'),
        ('E_P', 'Encargado de produccion'),
        ('D_G', 'Director General'),
        ('I_C', 'Ingeniero de campo'),
        ('G_C', 'Gerente de cuadrilla'),
        ('C_C', 'Capataz de cuadrilla'),
        ('C_T', 'Chofer de transporte'),
    )
    rol = models.CharField(max_length=3, choices=tipoUsuario, default='')

    def Mostrar(self):
        return "{} {} - {}".format(self.user.username, self.rol)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Trabajador'
        verbose_name_plural= 'Trabajadores'
        db_table= 'trabajador'
        ordering= ['id']

class Camion(models.Model):
    placa = models.CharField(max_length=20, blank = True)
    modelo = models.CharField(max_length=50, blank = True)
    capacidad = models.CharField(max_length=20, blank = True)
    estatusCamion = (
        ('C_A', 'Activo'),
        ('C_I', 'Inactivo'),
        ('C_M', 'Mantenimiento'),
    )
    estatus = models.CharField(max_length=3, choices=estatusCamion, default='Activo')
    idChofer = models.ForeignKey('Trabajador', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}, {}".format(self.estatus, self.modelo)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Camion'
        verbose_name_plural= 'Camiones'
        db_table= 'camion'
        ordering= ['id']

class MiembroCuadrilla(models.Model):
    nombre = models.CharField(max_length=20, blank = True)
    apellidoP = models.CharField(max_length=30, blank = True)
    apellidoM = models.CharField(max_length=30, blank = True)
    idCuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}, {}".format(self.nombre, self.apellidoP, self.apellidoM)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'MiembroC'
        verbose_name_plural= 'MiembrosC'
        db_table= 'miembroc'
        ordering= ['id']

class Cuadrilla(models.Model):
    nombre = models.CharField(max_length=20, blank = True)
    idGerenteCuadrilla = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    idCapatazCuadrilla = models.ForeignKey('Trabajador', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}, {}".format(self.nombre)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Cuadrilla'
        verbose_name_plural= 'Cuadrillas'
        db_table= 'cuadrilla'
        ordering= ['id']

class Productor(models.Model):
    nombre = models.CharField(max_length=20, blank = True)
    apellidoP = models.CharField(max_length=30, blank = True)
    apellidoM = models.CharField(max_length=30, blank = True)
    telefono = models.CharField(max_length=10, blank = True)

    def Mostrar(self):
        return "{}, {}".format(self.nombre, self.apellidoP, self.apellidoM)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Productor'
        verbose_name_plural= 'Productores'
        db_table= 'productor'
        ordering= ['id']

class Huerta(models.Model):
    nombre = models.CharField(max_length=20, blank = True)
    ubicacion = models.CharField(max_length=30, blank = True)
    estatusHuerta = (
        ('H_A', 'Activo'),
        ('H_I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=3, choices=estatusHuerta, default='Activo')
    idProductor = models.ForeignKey('Productor', on_delete=models.CASCADE)
    fruta = models.CharField(max_length=20, blank = True)

    def Mostrar(self):
        return "{}, {}".format(self.nombre, self.estatus)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Huerta'
        verbose_name_plural= 'MHuertas'
        db_table= 'huerta'
        ordering= ['id']

class Pedido(models.Model):
    nombreCliente = models.CharField(max_length=20, blank = True)
    apellidoPCliente = models.CharField(max_length=20, blank = True) 
    apellidoMCliente = models.CharField(max_length=20, blank = True)
    cantidad = models.FloatField(max_length=10, blank = True)
    tipoFruta = models.CharField(max_length=20, blank = True)
    fecha = models.DateField()
    calidadFruta = models.CharField(max_length=20, blank = True)
    estatusPedido = (
        ('P_C', 'Por cumplir'),
        ('Y_T', 'Terminado'),
    )
    estatus = models.CharField(max_length=3, choices=estatusPedido, default='Activo')

    def Mostrar(self):
        return "{}, {}".format(self.nombreCliente, self.estatus)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural= 'Pedidos'
        db_table= 'pedido'
        ordering= ['id']

class OrdenCorte(models.Model):
    cantidad = models.FloatField(max_length=10, blank = True)
    tipoFruta = models.CharField(max_length=20, blank = True)
    fecha = models.DateField()
    calidadFruta = models.CharField(max_length=20, blank = True)
    estatusOrden = (
        ('P_C', 'Por cumplir'),
        ('Y_T', 'Terminado'),
    )
    estatus = models.CharField(max_length=3, choices=estatusOrden, default='Activo')
    idViaje = models.ForeignKey('Viaje', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}, {}".format(self.nombreCliente, self.estatus)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural= 'Pedidos'
        db_table= 'pedido'
        ordering= ['id']

class Viaje(models.Model):
    fecha = models.DateField()
    horaSalida = models.TimeField(max_length=20, blank = True)
    horaLlegada = models.TimeField(max_length=20, blank = True)
    estatusViaje = (
        ('P_R', 'Por realizar'),
        ('V_R', 'Realizado'),
    )
    estatus = models.CharField(max_length=3, choices=estatusViaje, default='Activo')
    idOrden = models.ForeignKey('OrdenCorte', on_delete=models.CASCADE)
    idCamion = models.ForeignKey('Camion', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{}, {}".format(self.nombreCliente, self.estatus)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural= 'Pedidos'
        db_table= 'pedido'
        ordering= ['id']

class ReporteCorte(models.Model):
    fecha = models.DateField()
    idCuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to = 'Reportes/Corte')

    def Mostrar(self):
        return "{}, {}".format(self.fecha)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'ReporteCorte'
        verbose_name_plural= 'ReportesCortes'
        db_table= 'reportecorte'
        ordering= ['id']
