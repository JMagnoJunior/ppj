# -*- coding: utf-8 -*-
""" Este modulo contém as views para apresentação dos slides sobre a linguagem """
from pyramid.view import view_config

# pylint: disable=W0613,C0111
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

@view_config(route_name='slide10', renderer='templates/slides/slide10.jinja2')
def slide10(request):
    return {}

@view_config(route_name='fim', renderer='templates/slides/fim.jinja2')
def fim(request):
    return {}

@view_config(route_name='produto_ws', renderer='templates/slides/detalhe_produto.jinja2')
def exemplo_web_service(request):
    #import suds
    #cliente = suds.client.Client("https://jhom2.correiosnet.int/produtoservice/produtoService/produtoWS?wsdl ", \
    #                             username = "9571", password = "bcsteste")
    #produto = cliente.service.consultaProduto(codigoProduto = request.matchdict["codigo_produto"])
    produto = 'teste'
    return {"produto":produto}