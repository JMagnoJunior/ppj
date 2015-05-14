# -*- coding: utf-8 -*-
""" Este modulo contém as regras de negócio do sistema """
from sqlalchemy import (Column, Index, Integer, Unicode, Date, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker, synonym)
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import relationship
from datetime import date
from ppj.util import enum

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

# -- Enums -- #
Sexo = enum(MASCULINO='M', FEMININO='F')

# -- Classes -- #
class Cliente(Base):
    """Representa os clientes da empresa
    """
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(Unicode, unique=True)
    _data_nascimento = Column('data_nascimento',Date)
    sexo = Column(Unicode)
    estado_civil = Column(Unicode)
    dependentes = relationship("Dependente", backref="dono_conta")
    
    def __init__(self, nome, data_nascimento, sexo, estado_civil):
        """O construtor da classe exige que seja informado
           o nome, data_nascimento, sexo e estado estadocivil do cliente
        """
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil

    def as_dict(self):
        """Retorna um dicionario para facilitar a adatação da a classe para json
        """
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        from util import formata_data
        self._data_nascimento = formata_data(value)     

    data_nascimento = synonym('_data_nascimento', descriptor=data_nascimento)

    @property
    def e_cliente_especial(self):
        """
        Se a idade do cliente for maior que 18 anos, entao ele deve ser considerado e_adulto.
        >>> c = Cliente('Wellington','1990-01-01','M','Solteiro')
        >>> c.e_cliente_especial
        True
        """
        result = True if self.data_nascimento >= date(1970, 01, 01) else False
        return result            

class Dependente(Base):
    """Representa os dependentes dos clientes
    """
    __tablename__ = "dependente"

    id = Column(Integer, primary_key=True)
    nome = Column(Unicode)
    sexo = Column(Unicode)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))

    def __init__(self,nome,sexo):
        self.nome = nome
        self.sexo = sexo

    def as_dict(self):
        """ Retorna um dicionario para facilitar a adaptação da classe para json
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  