# coding: utf-8

from django.contrib import admin
from .models import Cliente, Pedido, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone')
    list_display_links = ('nome', 'fone')
    search_fields = ('nome', 'fone', 'email')

class PizzaInline(admin.TabularInline):
    model = Pizza

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente',
            'data_hora_pedido', 'data_hora_despacho', 'partiu')
    list_display_links = ('data_hora_pedido', )
    list_filter = ('cliente', )
    inlines = [PizzaInline]

    def partiu(self, object):
        return bool(object.data_hora_despacho)

    partiu.boolean = True


admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Pedido, PedidoAdmin)
