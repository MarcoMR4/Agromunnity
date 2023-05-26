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
    path('help', views.help, name='help'),
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
    path('vs/',views.viewSquad, name="vs"),
    #Transporte
    path('t/',views.transport, name="t"),
    path('td/',views.transportDelete, name="td"),
    path('tr/',views.transportRegister, name="tr"),
    path('tm/',views.transportModify, name="tm"),
    #Pedido
    path('so/',views.order, name="so"),
    path('som/',views.orderModify, name="som"),
    path('sor/',views.orderRegister, name="sor"),
    path('sod/',views.orderDelete, name="sod"),
    path('vso/',views.viewOrder, name="vso"),
    #Huerta
    path('o/',views.orchard, name="o"),
    path('om/',views.orchardModify, name="om"),
    path('or/',views.orchardRegister, name="or"),
    path('od/',views.orchardDelete, name="od"),
    path('vo/',views.viewOrchard, name="vo"),
    #Viaje
    path('ct/',views.trip, name="ct"),
    path('ctm/',views.tripModify, name="ctm"),
    path('ctr/',views.tripRegister, name="ctr"),
    path('ctd/',views.tripDelete, name="ctd"),
    path('mt/',views.myTrips, name="mt"),
    #Orden de corte
    path('co/',views.courtOrder, name="co"),
    path('com/',views.courtOrderModify, name="com"),
    path('cor/',views.courtOrderRegister, name="cor"),
    path('cod/',views.courtOrderDelete, name="cod"),
    #Cliente
    path('c/',views.client, name="c"),
    path('cm/',views.clientModify, name="cm"),
    path('cr/',views.clientRegister, name="cr"),
    path('cd/',views.clientDelete, name="cd"),
    #Calidad y calibre
    path('q/',views.quality, name="q"),
    path('qmc/',views.qualityModifyCaliber, name="qmc"),
    path('qmq/',views.qualityModifyQuality, name="qmq"),
    path('qrc/',views.qualityRegisterCaliber, name="qrc"),
    path('qdc/',views.qualityDeleteCaliber, name="qdc"),
    path('qrq/',views.qualityRegisterQuality, name="qrq"),
    path('qdq/',views.qualityDeleteQuality, name="qdq"),
    #Incidente
    path('i/',views.incident, name="i"),
    path('id/',views.incidentDelete, name="id"),
    path('ir/',views.incidentRegister, name="ir"),
    #Cambiar estatus inocuidad huerta
    path('ss/',views.safetyStatus, name="ss"),
    path('ssm/',views.safetyStatusModify, name="ssm"),
    #Finalizar Proceso
    path('ft',views.finishTrip, name="ft"),
    path('ftr/',views.finishTripRegister, name="ftr"),
    #Mis cuadrillas
    path('ms/',views.mySquad, name="ms"),
    path('msd/',views.mySquadDelete, name="msd"),
    path('msr/',views.mySquadRegister, name="msr"),
    path('msm/',views.mySquadModify, name="msm"),
    path('msmd/',views.mySquadMemberDelete, name="msmd"),
    path('msmr/',views.mySquadMemberRegister, name="msmr"),
    path('msmm/',views.mySquadMemberModify, name="msmm"),
    path('msms/',views.mySquadMemberSave, name="msms"),
    #Jefe de cuadrilla
    path("sl/", views.squadLeader, name="sl"),
    path("slr/", views.squadLeaderRegister, name="slr"),
    path("sld/", views.squadLeaderDelete, name="sld"),
    path("slm/", views.squadLeaderModify, name="slm"),
    #Solucion de incidencias
    path('si/',views.solveIncident, name="si"),
    path('sid/',views.solveIncidentDelete, name="sid"),
    path('sir/',views.solveIncidentRegister, name="sir"),
    #Precios autorizados
    path("ap/", views.authorizedPrice, name="ap"),
    path("apd/", views.authorizedPriceDelete, name="apd"),
    path("apm/", views.authorizedPriceModify, name="apm"),
    path("apr/", views.authorizedPriceRegister, name="apr"),
    #Fruta Huerta
    path("f/", views.fruit, name="f"),
    path("fd/", views.fruitDelete, name="fd"),
    path("fm/", views.fruitModify, name="fm"),
    path("fr/", views.fruitRegister, name="fr"),
    #Roles
    path("r/", views.rol, name="r"),
    path("rd/", views.rolDelete, name="rd"),
    path("rm/", views.rolModify, name="rm"),
    path("rr/", views.rolRegister, name="rr"),
    #Reportes de corte
    path("rp/", views.report, name="rp"),
    path("rpd/", views.reportDelete, name="rpd"),
    path("rpm/", views.reportModify, name="rpm"),
    path("rpr/", views.reportRegister, name="rpr"),
]



if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)