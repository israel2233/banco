from django.db import models

# Create your models here

class Cuentas(models.Model):
    identificacion = models.CharField(max_length = 10 )
    nombre = models.CharField(max_length = 30, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 30, verbose_name = 'Apellido')
    direccion = models.CharField(max_length = 50, verbose_name = 'Dirección')
    telefono = models.CharField('Teléfono', max_length = 10)
    correo_electronico = models.EmailField('Correo Electronico',blank = True, null = True)
    contrasenia = models.CharField('Passwd', max_length=128)
    numero_cuenta = models.CharField('Numero de Cuenta',max_length=7)
    fecha_creacion = models.DateField('Fecha de creación', auto_now_add=True)
    tipo_cuenta = models.CharField('Tipo de Cuenta', max_length=10)
    saldo = models.FloatField('Saldo')
    nombre_usuario = models.CharField('Nombre de Usuario', max_length= 20)

    def __str__(self):
        return self.numero_cuenta