#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from operacion import models as operacion

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Tipo de actividad"
        verbose_name_plural = "Tipo de actividades"
    # end class

    def __unicode__(self):
        return u'%s' % self.nombre
    # end def
# end class


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField("Descripción", max_length=400)
    equipo = models.ForeignKey(operacion.Equipo)
    tipo_de_actividad = models.ForeignKey(TipoActividad)
    fecha_de_ejecucion = models.DateField()
    repetir_cada = models.TextField(default=0)
    unidad_de_repeticion = models.IntegerField(choices=(
        (3, "Mes(es)", ), (4, "Año(s)", ), ), null=True, blank=True, default=3)
    # Por cuando se repite

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
    # end class

    def __unicode__(self):
        return u'%s' % self.nombre
    # end def
# end class
