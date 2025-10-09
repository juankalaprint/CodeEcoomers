from django.contrib import admin
from .models import Categoria
# Register your models here.
#admin.site.register(Categoria)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_Categoria', 'slug', 'descripcion')
    prepopulated_fields = {'slug': ('nombre_Categoria',)}
    search_fields = ('nombre_Categoria', 'descripcion')
    list_filter = ('nombre_Categoria',)
    list_per_page = 20
