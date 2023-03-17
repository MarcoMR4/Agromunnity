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
    path('logout/', views.lo, name='exit')
]



if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)