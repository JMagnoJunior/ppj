from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (  DBSession, Base,  )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # Slides
    config.add_route('index', '/')
    config.add_route('slide1', 'slide1')
    config.add_route('slide2', 'slide2')
    config.add_route('slide3', 'slide3')
    config.add_route('slide4', 'slide4')
    config.add_route('slide5', 'slide5')
    config.add_route('slide6', 'slide6')
    config.add_route('slide7', 'slide7')
    config.add_route('slide8', 'slide8')
    config.add_route('slide9', 'slide9')
    config.add_route('slide10', 'slide10')
    config.add_route('fim', 'fim')
    # PPJ - Python
    config.add_route('index_cliente', 'index_cliente')
    config.add_route('clientes', 'clientes')
    config.add_route('inclusao_cliente', 'incluir/cliente')
    config.add_route('cliente', 'cliente/{nome}')
    config.add_route('add_dependente', 'add_dependente')
    config.add_route('inclui_cliente', 'inclui/cliente')
    config.add_route('edita_cliente', 'editar/cliente/{id}')
    config.add_route('consulta_dependentes', 'consulta_dependentes')
    config.add_route('dependentes', 'dependentes')
    config.add_route('produto_ws', 'produto/{codigo_produto}')

    config.scan()
    return config.make_wsgi_app()
