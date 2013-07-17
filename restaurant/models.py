# -*- coding: utf-8 -*-
from django.db import models
from multiling import MultilingualModel
import os
# Create your models here.


def get_image_mesas_path(instance, filename):
    return os.path.join('mesas', str(instance.id), filename)


def get_image_plato_path(instance, filename):
    return os.path.join('platos', str(instance.id), filename)


class Mesa(models.Model):
    class Meta:
        verbose_name = ('Mesa')
        verbose_name_plural = ('Mesas')

    numero = models.CharField(max_length=50, verbose_name='Número')
    disponible = models.BooleanField()
    codigoqr = models.ImageField(upload_to=get_image_mesas_path)

    def __unicode__(self):
        return self.numero


class CategoriaPlato(models.Model):
    class Meta:
        verbose_name = ('CategoriaPlato')
        verbose_name_plural = ('CategoriaPlatos')

    nombre = models.CharField(max_length=100, verbose_name=u'Número')


class Plato(models.Model):
    class Meta:
        verbose_name = ('Plato')
        verbose_name_plural = ('Platos')

    nombre = models.CharField(max_length=100, verbose_name=u'Nombre')
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to=get_image_plato_path)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaPlato, related_name='categoria_de_plato')
    ingredientes = models.ManyToManyField("Ingrediente", related_name='ingredientes_por_plato', blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Lenguaje(models.Model):

    class Meta:
        verbose_name = ('Lenguaje')
        verbose_name_plural = ('Lenguajes')

    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=16)


class IngredienteTraduccion(models.Model):

    class Meta:
        verbose_name = ('IngredienteTraduccion')
        verbose_name_plural = ('IngredienteTraducciones')

    lenguaje = models.ForeignKey(Lenguaje)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    model = models.ForeignKey("Ingrediente")


class Ingrediente(MultilingualModel):

    class Meta:
        translation = IngredienteTraduccion
        multilingual = ['nombre', 'descripcion']


class Orden(models.Model):

    class Meta:
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')

    mesa = models.ForeignKey(Mesa)
    preparacion = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.mesa


class DatalleOrden(models.Model):

    class Meta:
        verbose_name = ('DatalleOrden')
        verbose_name_plural = ('DatallesOrden')

    orden = models.ForeignKey(Orden, related_name="orden_in_detalle")
    platillo = models.ForeignKey(Plato, related_name="platillo_orden")
    anotacion = models.TextField()

    def __unicode__(self):
        return str(self.orden) + " " + str(self.plato)


class Cliente(models.Model):
    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    dni = models.CharField(max_length=8, verbose_name="DNI")
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre + " " + self.apellidos


class Pago(models.Model):
    class Meta:
        verbose_name = ('Pago')
        verbose_name_plural = ('Pagos')

    orden = models.ForeignKey(Orden, related_name="orden_pago")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, related_name="cliente_pago", blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.orden) + " -> " + str(self.precio)
