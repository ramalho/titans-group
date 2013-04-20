# coding: utf-8

from __future__ import unicode_literals

import sys

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    fone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64, blank=True)
    logradouro = models.CharField(max_length=128, blank=True)
    numero = models.PositiveIntegerField(default=0)
    desconto = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.fone)

    # 2TO3: compatível Python 2 e Python 3
    if sys.version_info.major == 3:
        __str__ == __unicode__



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    data_hora_pedido = models.DateTimeField(auto_now_add=True)
    data_hora_despacho = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '#%s - %s' % (self.id, self.data_hora_pedido)

SABORES = [
    ('',            '-'),
    ('queijo',      'muçarela'),
    ('calabreza',   'calabreza'),
    ('atum',        'atum'),
    ('frango-cat',  'frango com catupiry'),
    ('chocolate',   'chocolate'),
]

class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor1 = models.CharField(max_length=16, choices=SABORES)
    sabor2 = models.CharField(max_length=16, choices=SABORES, blank=True)
    borda_recheada = models.BooleanField()

    def __unicode__(self):
        if not self.sabor2:
            cobertura = self.sabor1
        else:
            cobertura = '1/2 %s, 1/2 %s' % (self.sabor1, self.sabor2)
        borda = ' +borda recheada' if self.borda_recheada else ''
        return cobertura+borda

