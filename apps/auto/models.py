from django.db import models
from apps.user.models import User
from apps.modelo.models import Model

class Auto(models.Model):
    placa = models.CharField(max_length=50, verbose_name="Auto")
    kilometraje = models.PositiveIntegerField(verbose_name="Kilometraje", default=0)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="Usuario")
    modelo = models.ForeignKey(Model, on_delete=models.SET_NULL,  null=True,verbose_name="Modelo")

    class Meta: 
        verbose_name = "Auto"
        verbose_name_plural = "Autos"
    
    def __str__(self):
        return '%s %s' % (self.placa, self.kilometraje)
