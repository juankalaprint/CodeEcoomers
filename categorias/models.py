from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre_Categoria = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    descripcion = models.TextField(max_length=400, blank=True)
    def _str_(self):
        return self.nombre_Categoria
    def get_url(self):
        return reverse('productos_por_categoria', args=[self.slug])
    
    