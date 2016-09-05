from supra import views as supra
import forms 
import models

class RegistroSupraForm(supra.SupraFormView):
	model = models.Registro
	def get_form_class(self):
		self.get_form_kwargs()
		if self.instance and self.request.user.pk == self.instance.operario.pk:
			self.form = forms.RegistroEditForm.make(self.instance)
		else:
			self.form = forms.RegistroCreateForm
		#end if
		return self.form
	#end def
# end class


class RegistroCreateSupraForm(supra.SupraFormView):
	model = models.Registro
	form_class = forms.RegistroCreateForm
# end class

class CampoListView(supra.SupraListView):
	model = models.Campo
	list_display = ['nombre', 'tipo__nombre', 'formulario']

# end def