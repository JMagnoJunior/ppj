import os
import sys
import transaction
import datetime

from sqlalchemy import engine_from_config
from pyramid.paster import ( get_appsettings, setup_logging,  )
from pyramid.scripts.common import parse_vars
from ..models import ( DBSession, Cliente, Base, Dependente )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        cliente = Cliente(nome='Wellington', data_nascimento=datetime.date.today(),sexo='M',estado_civil='Casado')
        dependente1 = Dependente(nome="Sofia",sexo="F")
        dependente2 = Dependente(nome="Pedro",sexo="M")
        cliente.dependentes.append(dependente1)
        cliente.dependentes.append(dependente2)
        
        cliente2 = Cliente(nome='Joao', data_nascimento=datetime.date.today(),sexo='M',estado_civil='Casado')
        DBSession.add(cliente)
        DBSession.add(cliente2)
