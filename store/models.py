from django.db import models
from categorias.models import Categoria
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=400, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='imgs/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
