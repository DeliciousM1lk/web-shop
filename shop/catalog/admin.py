from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at')
    list_display_links = ('id','name')
    search_fields = ('name', 'description')
    list_per_page = 10


