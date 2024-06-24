from django.db import models
from usuarios.models import Usuario

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    editorial = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacion = models.PositiveIntegerField()
    idioma = models.CharField(max_length=50)
    numero_paginas = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.titulo