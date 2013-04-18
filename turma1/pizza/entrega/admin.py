# coding: utf-8

from django.contrib import admin
from .models import Cliente, Pedido

admin.site.register(Cliente)
admin.site.register(Pedido)
