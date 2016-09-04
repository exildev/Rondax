from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX, DateRangeEX
import models

admin_site._registry = admin.site._registry
admin_site.register(models.Operario)
