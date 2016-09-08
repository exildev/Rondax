# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=400)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Planta(models.Model):
    nombre = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa)
    ciudad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return u'%s %s Ciudad:%s' % (self.nombre, self.empresa.nombre, self.ciudad.nombre)
    # end def
# end class


class Unidad(models.Model):
    nombre = models.CharField(max_length=200)
    planta = models.ForeignKey(Planta)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
    # end class

    def __unicode__(self):
        return u'%s Planta: %s' % (self.nombre, self.planta.nombre)
    # end def
# end class


class Turno(models.Model):
    nombre = models.CharField(max_length=200)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400)
    unidad = models.ForeignKey(Unidad)

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    # end def
# end class
