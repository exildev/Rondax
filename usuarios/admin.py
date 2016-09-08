from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX
import models
import forms


class OperarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'turno')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('turno',)
    form = forms.OperarioForm


admin_site._registry = admin.site._registry
admin_site.register(models.Operario, OperarioAdmin)
