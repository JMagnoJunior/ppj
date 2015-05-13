# -*- coding: utf-8 -*-
from sqlalchemy import ( Column, Index, Integer, Unicode, Date, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import ( scoped_session, sessionmaker, )
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import relationship, backref
from datetime import date
from util import enum


#-----------------------

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

#-----------------------
# Isso é um ENUM!
Sexo = enum(MASCULINO='M', FEMININO='F')

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(Unicode,unique=True)
    data_nascimento = Column(Date)
    sexo = Column(Unicode)
    estado_civil = Column(Unicode)
    dependentes = relationship("Dependente",backref="dono_conta")

    def __init__(self,nome,data_nascimento,sexo,estado_civil):
        self.nome = nome
        if type(data_nascimento) is not date :
            data_split = data_nascimento.split('-')
            self.data_nascimento = date(int(data_split[0]),int(data_split[1]),int(data_split[2]) )
        else:
            self.data_nascimento = data_nascimento 
        self.sexo = sexo
        self.estado_civil = estado_civil

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def e_cliente_especial(self):
        """
        Se a idade do cliente for maior que 18 anos, entao ele deve ser considerado e_adulto.
        >>> c = Cliente('Wellington','1990-01-01','M','Solteiro')
        >>> c.e_cliente_especial()
        True
        """
        if self.data_nascimento >= date(1970,01,01):
            return True
        else :
            return False


class Dependente(Base):
    __tablename__ = "dependente"

    id = Column(Integer, primary_key=True,)
    nome = Column(Unicode)
    sexo = Column(Unicode)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))

    def __init__(self,nome,sexo):
        self.nome = nome
        self.sexo = sexo

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  

#-----------------

