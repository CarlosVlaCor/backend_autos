from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Type(models.IntegerChoices):
        ADMIN = (0, "Admin")
        CLIENTE = (1, "Cliente")
    
    type = models.IntegerField(verbose_name="Tipo", choices=Type.choices, default=Type.CLIENTE)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural ="Usuarios"
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
