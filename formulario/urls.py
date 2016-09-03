from django.conf.urls import include, url
from formulario import views

urlpatterns = [
	url(r'^form/registro/(?P<pk>\d+)/$', views.RegistroSupraForm.as_view(), name='form_registro'),
	url(r'^form/registro/create/$', views.RegistroCreateSupraForm.as_view(), name='form_crear_registro'),
]