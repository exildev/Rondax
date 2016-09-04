#from huella.admin import admin_site
from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX, DateRangeEX
import unicodedata
import models
import forms

class CampoInline(admin.TabularInline):
	model = models.Campo
	form = forms.CampoForm

class FormularioAdmin(admin.ModelAdmin):
	search_fields = ('nombre', 'fecha')
	list_filter = ('fecha', )
	list_display = ('nombre', 'equipo','fecha')
	model=models.Formulario
	form = forms.FormularioForm
	inlines = [CampoInline]
#end class

class RegistroAdmin(admin.ModelAdmin):
	model = models.Registro
	search_fields = ('formulario__nombre', 'operario___operario__nombre', 'operario___operario__apellido', 'fecha')
	list_filter = ('formulario', 'completado', 'fecha')
	list_display = ('formulario', 'nombre_operario', 'completado', 'fecha')
	def nombre_operario(self, obj):
		return "%s %s" % (obj.operario.first_name, obj.operario.last_name)
	#end def

	def get_form(self, request, obj=None, *args, **kwargs):
		if obj and request.user.pk == obj.operario.pk:
			self.form = forms.RegistroEditForm.make(obj)
		else:
			self.form = forms.RegistroCreateForm
		#end if
		return self.form
	#end def
#end class


admin_site.register(models.Tipo)
#admin.site.register(models.Campo)
admin_site.register(models.Formulario, FormularioAdmin)
#admin.site.register(models.Valor)
#admin.site.register(models.Entrada)
admin_site.register(models.Registro, RegistroAdmin)
