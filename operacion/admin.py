from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX, DateRangeEX
import models

admin_site.register(models.Empresa)
admin_site.register(models.Ciudad)
admin_site.register(models.Planta)
admin_site.register(models.Unidad)
admin_site.register(models.Turno)
admin_site.register(models.Equipo)
