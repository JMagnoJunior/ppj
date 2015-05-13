# -*- coding: utf-8 -*-
""" Este modulo contém todas as views do projeto PPJ """
import transaction
import json
import datetime
from pyramid.view import view_config
from sqlalchemy.exc import (DBAPIError, IntegrityError)
from .models import (DBSession, Cliente, Dependente)

# -- apresentacao -- #
@view_config(route_name='index', renderer='templates/apresentacao.jinja2')
def index(request):
    return {}

@view_config(route_name='slide1', renderer='templates/slides/slide1.jinja2')
def slide1(request):
    return {}

@view_config(route_name='slide2', renderer='templates/slides/slide2.jinja2')
def slide2(request):
    return {}

@view_config(route_name='slide3', renderer='templates/slides/slide3.jinja2')
def slide3(request):
    return {}

@view_config(route_name='slide4', renderer='templates/slides/slide4.jinja2')
def slide4(request):
    return {}

@view_config(route_name='slide5', renderer='templates/slides/slide5.jinja2')
def slide5(request):
    return {}

@view_config(route_name='slide6', renderer='templates/slides/slide6.jinja2')
def slide6(request):
    return {}

@view_config(route_name='slide7', renderer='templates/slides/slide7.jinja2')
def slide7(request):
    return {}

@view_config(route_name='slide8', renderer='templates/slides/slide8.jinja2')
def slide8(request):
    return {}    

@view_config(route_name='slide9', renderer='templates/slides/slide9.jinja2')
def slide9(request):
    return {}    

# ----------------------------------------
# -- Cliente  -- #
@view_config(route_name='index_cliente', renderer='templates/base.jinja2')
def index_cliente(request):
    return {}

@view_config(route_name='inclusao_cliente', renderer='templates/inclusao_cliente.jinja2')
def inclusao_cliente(request):
    return{}

@view_config(route_name='add_dependente', renderer='templates/formulario_dependente.jinja2')
def add_dependente(request):
    return{}

@view_config(route_name='clientes', renderer='templates/tabela_cliente.jinja2')
def lista_clientes(request):
    nome, data_nascimento, sexo, estado_civil = request.GET['nome'], \
    request.GET['data_nascimento'], request.GET['sexo'], \
    request.GET['estado_civil']

    query = DBSession.query(Cliente)
    query = query.filter(Cliente.nome.contains(nome)) if nome is not u'' else query
    query = query.filter(Cliente.data_nascimento == data_nascimento) if data_nascimento is not u'' else query
    query = query.filter(Cliente.sexo == sexo) if sexo is not u'' else query
    query = query.filter(Cliente.estado_civil == estado_civil) if estado_civil is not u'' else query        
    clientes = query.all()        
    return {"clientes":clientes}

@view_config(route_name='cliente', renderer='templates/detalhe_cliente.jinja2')
def detalhe_cliente(request):
    nome = request.matchdict['nome']

    query = DBSession.query(Cliente)
    query = query.filter(Cliente.nome.contains(nome)) if nome is not u'' else query
    cliente = query.one()
    return {"cliente":cliente}

@view_config(route_name='inclui_cliente', renderer='templates/resultado.jinja2')
def inclui_cliente(request):
    nome, data_nascimento, sexo, estado_civil = request.json_body['nome'], \
    request.json_body['data_nascimento'], request.json_body['sexo'], \
    request.json_body['estado_civil']

    dependentes = []
    for dep in request.json_body['dependentes']:
        dependente = Dependente(dep['nome'], dep['sexo'])
        dependentes.append(dependente)

    cliente = Cliente(nome, data_nascimento, sexo, estado_civil)    
    cliente.dependentes = dependentes

    with transaction.manager:   
        DBSession.add(cliente)
    return {"mensagem_sucesso":u'registro gravado com sucesso'}

@view_config(route_name='edita_cliente', renderer='templates/resultado.jinja2')
def edita_cliente(request):
    id = request.matchdict["id"]
    nome, sexo, estado_civil, data_json = request.json_body['nome'], request.json_body['sexo'], request.json_body['estado_civil'], request.json_body['data_nascimento'].split("-")
    data_nascimento = datetime.date(int(data_json[0]), int(data_json[1]), int(data_json[2]))
    
    cliente = DBSession.query(Cliente).filter(Cliente.id == id).one()
    cliente.nome, cliente.data_nascimento, cliente.sexo, cliente.estado_civil = nome, data_nascimento, sexo, estado_civil
    DBSession.flush()
    return {"mensagem_sucesso":u'registro gravado com sucesso'}

# -- dependentes -- #
@view_config(route_name='consulta_dependentes', renderer='templates/consulta_dependentes.jinja2')
def consulta_dependentes(request):
    return {}

@view_config(route_name='dependentes', renderer='templates/tabela_dependentes.jinja2')
def lista_dependentes(request):
    nome,sexo = request.GET['nome'], request.GET['sexo']
    query = DBSession.query(Dependente)
    query = query.filter(Dependente.nome.contains(nome)) if nome is not u'' else query
    query = query.filter(Dependente.sexo == sexo) if sexo is not u'' else query
    dependentes = query.all()     
    return {"dependentes":dependentes}

# --- Tratamento de Erro -- #

@view_config(context=DBAPIError, renderer="templates/resultado.jinja2")
def failed_validation(exc, request):
    print exc
    return {"mensagem_erro":u'Ocorreu um erro de conexão com o banco!'}

@view_config(context=IntegrityError, renderer="templates/resultado.jinja2")
def failed_validation(exc, request):
    print exc
    return {"mensagem_erro":u'Registro já cadastrado!'}
