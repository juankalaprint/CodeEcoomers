from django.contrib import admin
from .models import Auth
admin.site.register(Auth)


admin.site.site_header = 'Nombre personalizado'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Título en la pestaña del navegador'


