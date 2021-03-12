from django.db import models

# Create your models here.
class Clientes(models.Model):
    identificacion = models.CharField(max_length = 10 )
    nombre = models.CharField(max_length = 30, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 30, verbose_name = 'Apellido')
    direccion = models.CharField(max_length = 50, verbose_name = 'Dirección')
    tfno = models.CharField('Teléfono', max_length = 10)
    email = models.EmailField(blank = True, null = True)


    def __str__(self):
        return self.nombre