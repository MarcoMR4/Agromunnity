from django.contrib import admin
from .models import Trabajador, RolTrabajador, Cliente, Productor, Pedido, Calibre, Calidad, PedidoCalibreCalidad, OrdenCorte, ViajeCorte, ReporteCorte, ViajeCorte, CamionTransporte, Cuadrilla, OrdenCorte, Huerta, MiembroCuadrilla

admin.site.register(Trabajador)
admin.site.register(ViajeCorte)
admin.site.register(CamionTransporte)
admin.site.register(Cuadrilla)
admin.site.register(OrdenCorte)
admin.site.register(Huerta)
admin.site.register(MiembroCuadrilla)
admin.site.register(RolTrabajador)
admin.site.register(Cliente)
admin.site.register(Productor)
admin.site.register(Pedido)
admin.site.register(Calibre)
admin.site.register(PedidoCalibreCalidad)
admin.site.register(Calidad)
admin.site.register(ReporteCorte)