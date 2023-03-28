from django.contrib import admin
from .models import Trabajador, Viaje, Camion, Cuadrilla, OrdenCorte, Huerta, MiembroCuadrilla

admin.site.register(Trabajador)
admin.site.register(Viaje)
admin.site.register(Camion)
admin.site.register(Cuadrilla)
admin.site.register(OrdenCorte)
admin.site.register(Huerta)
admin.site.register(MiembroCuadrilla)