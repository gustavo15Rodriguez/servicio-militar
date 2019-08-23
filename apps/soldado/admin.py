from django.contrib import admin
from apps.soldado.models import Servicio, Soldado, Cuerpo

admin.site.register(Servicio)
admin.site.register(Soldado)
admin.site.register(Cuerpo)