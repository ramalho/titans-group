from django.shortcuts import render_to_response

from .models import Pizza

def pizzas_pendentes(request):
    lista = Pizza.objects.all().order_by('pedido')[:10]
    contexto = {'lista': lista}
    return render_to_response('entrega/pizzas_pend.html', contexto)
