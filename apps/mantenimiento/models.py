from django.db import models
from apps.auto.models import Auto

class Mantenimiento(models.Model):
    kilometraje = models.PositiveIntegerField(verbose_name="Kilometraje", default=0)
    descripcion = models.CharField(max_length=250, verbose_name="Descripcion")
    costo = models.PositiveSmallIntegerField(verbose_name="Costo", default=0)
    fecha = models.DateField(verbose_name="Fecha de inicio")
    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True,verbose_name="Auto")

    class Meta:
        verbose_name = "Mantenimiento"
        verbose_name_plural = "Mantenimientos"
    
    def __str__(self):
        return '%s %s %s %s' % (self.kilometraje, self.descripcion, self.costo, self.fecha)
