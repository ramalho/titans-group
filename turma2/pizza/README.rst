===================
Projeto Pizzaria
===================

--------------
Comandos úteis
--------------

Ativar o ambiente, a partir do diretório onde ele foi criado::

  $ source .django/bin/activate

Criar novas tabelas no BD::

  $ ./manage.py syncdb


Executar o servidor de desenvolvimento::

  $ ./manage.py runserver

Exportar dados::

  $ ./manage.py dumpdata entrega --indent=2 > entrega/fixtures/tres_clientes.json

Carregar dados::

  $ ./manage.py loaddata entrega/fixtures/tres_clientes.json

Remover uma tabela::

  $ ./manage.py dbshell
  sqlite> DROP TABLE entrega_cliente;
  sqilte> .quit





