from django.db import models

# Create your models here.
Class Categoria(models.Model):
    nombre_Categoria = models.CharField(max_length=50, unique=True)