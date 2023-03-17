from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    telefono = models.CharField(max_length=10, blank = True)
    correoPersonal = models.EmailField(max_length = 254, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TIPOUSER = (
        ('E_V', 'Encargado de ventas'),
        ('D_R', 'Director general'),
        ('E_A', 'Encargado de Acopio'),
        ('I_C', 'Ingeniero de campo'),
        ('E_B', 'Encargado de bitacora'),
        ('G_C', 'Gerente de cuadrillas'),
        ('E_P', 'Encargado de produccion'),
    )
    tipouser = models.CharField(max_length=3, choices=TIPOUSER, default='TU')

    def Mostrar(self):
        return "{} {} - {}".format(self.user.first_name, self.user.last_name, self.user.username)

    def __str__(self):
        return self.Mostrar()

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'
        db_table= 'usuarios'
        ordering= ['id']

