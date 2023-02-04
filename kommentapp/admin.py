from django.contrib import admin
from .models import KommentModel
@admin.register(KommentModel)
class KommentModelAdmin(admin.ModelAdmin):
    list_display = ('name','date',)
    readonly_fields = ('date',)
    search_fields = ('name','text',)
    list_filter= ('date',)
    
    
    
    
    
    """
    readonly_fields -поля только для чтения
    list_display - поля которые будут отображаться в списке объектов (столбцы)
    search_fields - поля по которым будет вестись поиск
    list_filter - поля по которым будет идти фильтрация
    list_editable - поля которые можно редактировать из списка объектов (сюда нельза писать 1-е поле из list_display)
    """