# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class IngredienteTraduccionInline(admin.StackedInline):
    model = IngredienteTraduccion
    extra = 1
    min_num = 1


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ["pk"]
    inlines = [IngredienteTraduccionInline]


admin.site.register(Ingrediente, IngredienteAdmin)

admin.site.register(Mesa)
admin.site.register(CategoriaPlato)
admin.site.register(Plato)
admin.site.register(Lenguaje)
admin.site.register(Orden)
admin.site.register(DatalleOrden)
admin.site.register(Cliente)
admin.site.register(Pago)