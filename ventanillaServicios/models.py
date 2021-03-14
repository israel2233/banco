from django.db import models
from balconServicios. models import Cuentas 

# Create your models here.
class Transacciones(models.Model):
    cuenta = models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    fecha = models.DateField('Fecha creacion', auto_now_add=True)
    numero_transaccion = models.CharField('Numero Transaccion', max_length=9)
    tipo = models.CharField("Tipo transaccion", max_length=10)
    concepto = models.CharField("Concepto del movimiento", max_length=64)
    monto = models.FloatField("Monto del movimiento")
    def __str__(self):
        return 'Transaccion #: '+self.numero_transaccion