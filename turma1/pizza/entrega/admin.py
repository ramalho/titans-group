# coding: utf-8

from django.contrib import admin
from .models import Cliente, Pedido, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone')
    list_display_links = ('nome', 'fone')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_hora_pedido', 'data_hora_despacho')
    list_display_links = ('data_hora_pedido', )

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Pedido, PedidoAdmin)

# XXX: temporario
admin.site.register(Pizza)

