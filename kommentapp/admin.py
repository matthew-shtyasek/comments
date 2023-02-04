from django.contrib import admin
from .models import KommentModel
@admin.register(KommentModel)
class KommentModelAdmin(admin.ModelAdmin):
    list_display = ('name','text','date')