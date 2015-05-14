#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import transaction
import json
from pyramid import testing
from .models import DBSession
import datetime

class TestClientes(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import ( Base, Cliente,Dependente ) 
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
                cliente = Cliente(nome=u'Wellington', data_nascimento='2000-01-01', sexo=u'M', estado_civil=u'Casado')
                dependente1 = Dependente(nome=u'Sofia', sexo=u'F')
                dependente2 = Dependente(nome=u'Pedro', sexo=u'M')
                cliente.dependentes.append(dependente1)
                cliente.dependentes.append(dependente2)        
                cliente2 = Cliente(nome=u'Joao', data_nascimento='2000-05-05', sexo=u'M', estado_civil=u'Casado')
                DBSession.add(cliente)
                DBSession.add(cliente2)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_deve_listar_clientes(self):
    	from .views import lista_clientes
    	request = testing.DummyRequest()
    	request.GET['nome'], request.GET['data_nascimento'], request.GET['sexo'], request.GET['estado_civil'] = u'Wellington', u'', u'', u''
    	result = lista_clientes(request)    	 
    	self.assertEqual(result['clientes'][0].nome, 'Wellington')

    def test_deve_exibir_detalhe_cliente(self):
        from .views import detalhe_cliente
        request = testing.DummyRequest()
        request.matchdict['nome'] = "Wellington"
        result = detalhe_cliente(request)
        self.assertEqual(result['cliente'].nome,'Wellington')
        self.assertEqual(result['cliente'].data_nascimento, datetime.date(2000,1,1))
        self.assertEqual(result['cliente'].sexo,'M')
        self.assertEqual(result['cliente'].estado_civil,'Casado')

    def test_deve_incluir_cliente(self):
    	from .views import inclui_cliente
    	request_body = {
            'nome': u'test',
            'sexo': u'F',
            'estado_civil': u'Solteiro',
            'data_nascimento': u'2000-05-05',
            'dependentes': u''
        }
        request = testing.DummyRequest(json_body = request_body, method = 'POST')
        request.matchdict["id"] = 1
        result = inclui_cliente(request)
        self.assertEqual(result['mensagem_sucesso'], u'registro gravado com sucesso')


    def test_deve_incluir_cliente_com_dependentes(self):
        from .views import inclui_cliente
        request_body = {
            'nome': u'test',
            'sexo': u'F',
            'estado_civil': u'Solteiro',
            'data_nascimento': u'2000-05-05',
            'dependentes' :[{u'sexo': u'M', u'nome': u'A1'}, {u'sexo': u'F', u'nome': u'A2'}]
        }
        request = testing.DummyRequest(json_body=request_body, method='POST')
        request.matchdict["id"] = 1
        result = inclui_cliente(request)
        self.assertEqual(result['mensagem_sucesso'], u'registro gravado com sucesso')

class TestUtil(unittest.TestCase):

    def test_deve_formatar_data(self):
        from .util import formata_data
        data = '2010-01-01'
        self.assertEqual(formata_data(data), datetime.date(2010, 1, 1))
        
        #self.assertEqual(isinstance(Sexo,type('Enum')),True)


# class TestMyViewSuccessCondition(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('sqlite://')
#         from .models import ( Base, MyModel, )        
#         DBSession.configure(bind=engine)
#         Base.metadata.create_all(engine)
#         with transaction.manager:
#             model = MyModel(name='one', value=55)
#             DBSession.add(model)

#     def tearDown(self):
#         DBSession.remove()
#         testing.tearDown()

#     def test_passing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'PPJ')


# class TestMyViewFailureCondition(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('sqlite://')
#         from .models import (Base, MyModel, )
#         DBSession.configure(bind=engine)

#     def tearDown(self):
#         DBSession.remove()
#         testing.tearDown()

#     def test_failing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info.status_int, 500)

