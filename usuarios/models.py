from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from operacion import models as operacion


class Operario(User):
    turno = models.ForeignKey(operacion.Turno)
# end class
# Create your models here.
