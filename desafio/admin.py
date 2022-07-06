from django.contrib import admin

from .models import CrearDios, DiosGriego, DiosRomano

# Register your models here.

admin.site.register(DiosGriego)
admin.site.register(DiosRomano)
admin.site.register(CrearDios)
