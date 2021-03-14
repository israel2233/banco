from django.urls import path
from ventanillaServicios import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ventanilla/', views.df, name='Ventanilla'),
    path('confirm/', views.confirm, name='Confirmacion' ),
    # path('error/', views.error, name='Error' ),
]