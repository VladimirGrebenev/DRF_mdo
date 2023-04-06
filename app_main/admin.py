from django.contrib import admin
from app_main import models


# Register your models here.

@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']


@admin.register(models.Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['id', 'modified_by', 'value']
