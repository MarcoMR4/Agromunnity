from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Trabajador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10, blank = True)
    rol = models.ForeignKey('RolTrabajador', on_delete=models.CASCADE)
    
    def Mostrar(self):
        return "{} {} - {}".format(self.usuario.first_name, self.usuario.last_name, self.rol.nombreRol)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Trabajador'
        verbose_name_plural= 'Trabajadores'
        db_table= 'trabajador'
        ordering= ['id']

class RolTrabajador(models.Model):
    nomenclaturaRol = models.CharField(max_length=3, blank = True)
    nombreRol = models.CharField(max_length=50, blank = True)

    def Mostrar(self):
        return "{} - {}".format(self.nomenclaturaRol, self.nombreRol)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'RolTrabajador'
        verbose_name_plural= 'RolesTrabajador'
        db_table= 'roltrabajador'
        ordering= ['id']

class CamionTransporte(models.Model):
    idChoferTransporte = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    capacidadTransporte = models.CharField(max_length=20, blank = True)
    placaTransporte = models.CharField(max_length=20, blank = True)
    modeloTransporte = models.CharField(max_length=50, blank = True)
    tipoTransporte = models.CharField(max_length=50, blank = True)
    descripcionTransporte = models.CharField(max_length=200, blank = True)
    candadoTransporte = models.CharField(max_length=20, blank = True)
    estatusCamion = (
        ('C_A', 'Activo'),
        ('C_I', 'Inactivo'),
        ('C_M', 'Mantenimiento'),
    )
    estatusTransporte = models.CharField(max_length=3, choices=estatusCamion, default='Activo')
    

    def Mostrar(self):
        return "{}, {} - {}".format(self.modeloTransporte, self.placaTransporte, self.estatusTransporte)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'CamionTransporte'
        verbose_name_plural= 'CamionesTransporte'
        db_table= 'camiontransporte'
        ordering= ['id']

class MiembroCuadrilla(models.Model):
    nombre = models.CharField(max_length=20, blank = True)
    apellidoP = models.CharField(max_length=30, blank = True)
    apellidoM = models.CharField(max_length=30, blank = True)
    noImss = models.CharField(max_length=30, blank = True)
    idCuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)

    def Mostrar(self):
        return "{} {} {}".format(self.nombre, self.apellidoP, self.apellidoM)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'MiembroC'
        verbose_name_plural= 'MiembrosC'
        db_table= 'miembroc'
        ordering= ['id']

class Cuadrilla(models.Model):
    idGerenteCuadrilla = models.ForeignKey('Trabajador', related_name='gerente', on_delete=models.CASCADE)
    idJefeCuadrilla = models.ForeignKey('Trabajador', related_name='jefe', on_delete=models.CASCADE)
    nombreCuadrilla = models.CharField(max_length=50, blank = True)
    ubicacionCuadrilla = models.CharField(max_length=50, blank = True)
    estatus = (
        ('C_A', 'Activa'),
        ('C_I', 'Inactiva'),
    )
    estatusCuadrilla = models.CharField(max_length=3, choices=estatus, default='Activa')

    def Mostrar(self):
        return "{} - {}".format(self.nombreCuadrilla, self.estatusCuadrilla)

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
        return "{} {} {}".format(self.nombre, self.apellidoP, self.apellidoM)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Productor'
        verbose_name_plural= 'Productores'
        db_table= 'productor'
        ordering= ['id']

class Huerta(models.Model):
    idProductor = models.ForeignKey('Productor', on_delete=models.CASCADE)
    nombreHuerta = models.CharField(max_length=50, blank = True)
    frutaHuerta = models.CharField(max_length=30, blank = True)
    ubicacionHuerta = models.CharField(max_length=50, blank = True)
    localizacionHuerta = models.CharField(max_length=300, blank = True)
    claveSagarpaHuerta = models.CharField(max_length=100, blank = True)
    estatusInocuidadHuerta = models.CharField(max_length=100, blank = True)
    estatus = (
        ('H_A', 'Activo'),
        ('H_I', 'Inactivo'),
    )
    estatusHuerta = models.CharField(max_length=3, choices=estatus, default='Activo')


    def Mostrar(self):
        return "{}, {}".format(self.nombreHuerta, self.estatusHuerta)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Huerta'
        verbose_name_plural= 'MHuertas'
        db_table= 'huerta'
        ordering= ['id']

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=40, blank = True)
    apellidoPCliente = models.CharField(max_length=20, blank = True) 
    apellidoMCliente = models.CharField(max_length=20, blank = True)
    rfcCliente = models.CharField(max_length=20, blank = True)

    def Mostrar(self):
        return "{} {} {}".format(self.nombreCliente, self.apellidoPCliente, self.apellidoMCliente)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'
        db_table= 'cliente'
        ordering= ['id']

class Pedido(models.Model):
    idTrabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    idCliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    numeroPedido = models.CharField(max_length=20, blank = True)
    fechaPedido = models.DateField()
    totalKilosPedido = models.IntegerField(blank=True)
    totalPalletsPedido = models.IntegerField(blank=True)
    estatusPedido = models.CharField(max_length=20, blank = True)
    mercadoPedido = models.CharField(max_length=20, blank = True)
    destinoPedido = models.CharField(max_length=20, blank = True)

    estatus = (
        ('P_P', 'Pendiente'),
        ('P_T', 'Terminado'),
    )
    estatusPedido = models.CharField(max_length=3, choices=estatus, default='Pendiente')

    def Mostrar(self):
        return "Pedido: {} - {}".format(self.numeroPedido, self.get_estatusPedido_display())

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural= 'Pedidos'
        db_table= 'pedido'
        ordering= ['id']

class Calibre(models.Model):
    numCalibre = models.IntegerField(blank=True)

    def Mostrar(self):
        return "Calibre: {}".format(self.numCalibre)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Calibre'
        verbose_name_plural= 'Calibres'
        db_table= 'calibre'
        ordering= ['id']

class Calidad(models.Model):
    descripcionCalidad = models.CharField(max_length=500, blank = True)
    numCalidad = models.IntegerField(blank=True)

    def Mostrar(self):
        return "Calidad: {}".format(self.numCalidad)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Calidad'
        verbose_name_plural= 'Calidades'
        db_table= 'calidad'
        ordering= ['id']

class PedidoCalibreCalidad(models.Model):
    idPedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    idCalibre = models.ForeignKey('Calibre', on_delete=models.CASCADE)
    idCalidad = models.ForeignKey('Calidad', on_delete=models.CASCADE)
    cantidadCC = models.IntegerField(blank=True)

    def Mostrar(self):
        return "Pedido: {} - {} kg.".format(self.idPedido, self.cantidadCC)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'PedidoCalibreCalidad'
        verbose_name_plural= 'PedidosCalibreCalidad'
        db_table= 'pedidocalibrecalidad'
        ordering= ['id']

class OrdenCorte(models.Model):
    fechaOrden = models.DateField()
    numeroOrden = models.CharField(max_length=20, blank = True)
    cantidadFruta = models.FloatField(max_length=10, blank = True)
    tipoFruta = models.CharField(max_length=20, blank = True)
    calidadFruta = models.CharField(max_length=20, blank = True)
    idHuerta = models.ForeignKey('Huerta', on_delete=models.CASCADE)
    tipoCorte = models.CharField(max_length=20, blank = True)
    estatus = (
        ('O_P', 'Pendiente'),
        ('O_T', 'Terminado'),
    )
    estatusOrden = models.CharField(max_length=3, choices=estatus, default='Pendiente')

    def Mostrar(self):
        return "Orden: {} - {}".format(self.numeroOrden, self.get_estatusOrden_display())

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'OrdenCorte'
        verbose_name_plural= 'OrdenesCorte'
        db_table= 'ordenCorte'
        ordering= ['id']

class ViajeCorte(models.Model):
    fechaViaje = models.DateField()
    idCamionTransporte = models.ForeignKey('CamionTransporte', related_name='principal', on_delete=models.CASCADE)
    idCamionSecundarioTransporte = models.ForeignKey('CamionTransporte', related_name='secundario', on_delete=models.CASCADE)
    horaSalida = models.TimeField(max_length=20, blank = True)
    horaLlegada = models.TimeField(max_length=20, blank = True)
    idOrdenCorte = models.ForeignKey('OrdenCorte', on_delete=models.CASCADE)
    idCuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)
    puntoReunion = models.CharField(max_length=500, blank = True)
    estatus = (
        ('V_P', 'No terminado'),
        ('V_T', 'Terminado'),
    )
    estatusViaje = models.CharField(max_length=3, choices=estatus, default='No terminado')

    def Mostrar(self):
        return "Viaje del dia: {} - {}".format(self.fechaViaje, self.get_estatusViaje_display())

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'ViajeCorte'
        verbose_name_plural= 'ViajesCorte'
        db_table= 'viajecorte'
        ordering= ['id']

class ReporteCorte(models.Model):
    fecha = models.DateField()
    idCuadrilla = models.ForeignKey('Cuadrilla', on_delete=models.CASCADE)
    documento = models.FileField(upload_to = 'Reportes/Corte')
    cajasCortadas = models.IntegerField(blank=True)
    observacionesReporte = models.CharField(max_length=500, blank = True)

    def Mostrar(self):
        return "Reporte del dia: {} - {} cajas cortadas.".format(self.fecha, self.cajasCortadas)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'ReporteCorte'
        verbose_name_plural= 'ReporteCortes'
        db_table= 'reportecorte'
        ordering= ['id']