from django.contrib import admin
from categorias.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_Categoria', 'slug', 'descripcion')
    prepopulated_fields = {'slug': ('nombre_Categoria',)}
    search_fields = ('nombre_Categoria', 'descripcion')
    list_filter = ('nombre_Categoria',)
    
    
