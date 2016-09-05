from supra import views as supra
import forms 
import models
from django.views.decorators.csrf import csrf_exempt

supra.SupraConf.ACCECC_CONTROL["allow"] = True

class RegistroSupraForm(supra.SupraFormView):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(RegistroSupraForm, self).dispatch(request, *args, **kwargs)
	# end def

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

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(RegistroSupraForm, self).dispatch(request, *args, **kwargs)
	# end def
	
	model = models.Registro
	form_class = forms.RegistroCreateForm
# end class

class CampoListView(supra.SupraListView):
	model = models.Campo
	list_display = ['nombre', 'tipo__nombre', 'formulario']
	list_filter = ['formulario']

# end def