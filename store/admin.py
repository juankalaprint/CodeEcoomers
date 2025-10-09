from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "is_available", "categories","updated_at",)
    prepopulated_fields = {'slug':('name',)}
    admin.site.register(models.Products,ProductAdmin)
