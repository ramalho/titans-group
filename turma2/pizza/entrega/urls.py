from django.conf.urls import patterns, include, url
from django.views import generic

from .views import pizzas_pendentes
from .models import Cliente

urlpatterns = patterns('',
    url(r'^$', pizzas_pendentes, name='pendentes'),
    url(r'^cli$', generic.list.ListView.as_view(model=Cliente) ),
    url(r'^cli/(?P<pk>\d+)$', generic.detail.DetailView.as_view(model=Cliente), name='cliente_detail' ),
)
