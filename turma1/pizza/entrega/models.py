# coding: utf-8

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    fone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64, blank=True)
    logradouro = models.CharField(max_length=128, blank=True)
    numero = models.PositiveIntegerField(default=0)
    desconto = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __unicode__(self):
        return u'%s (%s)' % (self.nome, self.fone)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    data_hora_pedido = models.DateTimeField()
    data_hora_despacho = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return u'#%s - %s' % (self.id, self.data_hora_pedido)
