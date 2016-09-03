from django.shortcuts import render
from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import models
supra.SupraConf.ACCECC_CONTROL["allow"] = True


# Create your views here.
class Login(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)
    # end def
    model = models.Operario
# end class
