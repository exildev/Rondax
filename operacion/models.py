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

    def __unicode__(self):
        return u'%s Planta: %s' % (self.nombre, self.planta.nombre)
    # end def
# end class


class Turno(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400)
    turno = models.ForeignKey(Turno)
    unidad = models.ForeignKey(Unidad)

    def __unicode__(self):
        return u'%s Turno:%s' % (self.nombre, self.turno.nombre)
    # end def
# end class
