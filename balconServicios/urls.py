from django.urls import path
from balconServicios import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pagina_principal, name='Home'),
    path('cuentas/', views.insertar_cuenta, name='Cuentas'),
    path('cuenta_c/', views.cuenta_creada, name= 'CuentaC')
]

