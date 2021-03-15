from django.urls import path
from bancaWeb import  views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login, name='Login'),
    path('consolidados/<str:id>', views.consolidado, name='Consolidado' ),
    path('historial/<str:cuenta>/', views.historial, name='Historial' ),
    path('transferencias/<str:cuenta>/', views.transaccion, name='Transaccion'),
    path('confirmacion/', views.confirm, name='ConfirmacionT' ),
    
]