#Agronomunnity URL Configuration
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    #administrador
    path('admin/', admin.site.urls),
    #usuarios en general
    path('', views.index, name='index'),
    path('login/', views.li, name='login'),
    path('logout/', views.lo, name='exit'),

    #Encargado de bitacora
    #Trabajador
    path("w/", views.worker, name="w"),
    path("wr/", views.workerRegister, name="wr"),
    path("wd/", views.workerDelete, name="wd"),
    path("wm/", views.workerModify, name="wm"),
    #Productor
    path('p/',views.producer, name="p"),
    path('pr/',views.producerRegister, name="pr"),
    path('pd/',views.producerDelete, name="pd"),
    path('pm/',views.producerModify, name="pm"),
    #Cuadrillas
    path('s/',views.squad, name="s"),
    path('sd/',views.squadDelete, name="sd"),
    path('sr/',views.squadRegister, name="sr"),
    path('sm/',views.squadModify, name="sm"),
    path('smd/',views.squadMemberDelete, name="smd"),
    path('smr/',views.squadMemberRegister, name="smr"),
    path('smm/',views.squadMemberModify, name="smm"),
    path('sms/',views.squadMemberSave, name="sms"),
    #Transporte
    path('t/',views.transport, name="t"),
    path('td/',views.transportDelete, name="td"),
    path('tr/',views.transportRegister, name="tr"),
    path('tm/',views.transportModify, name="tm"),
    #Pedido
    path('so/',views.order, name="so"),

    path('or/',views.orchardRegister, name="or"),
    path('om/',views.orchardModify, name="om")

]



if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)