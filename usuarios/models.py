# usuario/models.py
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.email
