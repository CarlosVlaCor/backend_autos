from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre de marca")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
    def __str__(self):
        return 'Nombre de la marca %s' % (self.nombre)

class Model(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del modelo") 
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, verbose_name="Marca")

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return '%s %s' % (self.nombre, self.marca.nombre)
    

