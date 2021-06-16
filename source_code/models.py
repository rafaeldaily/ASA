# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.sql.base import _entity_namespace
from sqlalchemy.sql.expression import extract
from sqlalchemy.sql.functions import modifier
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, DateTime, Float
from database import Base
    

##################################################################3

class Airport(Base):
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True)
    nome = Column(String(4), unique=True)

    def __init__(self, nome=None):
        self.nome = nome

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    origem = Column(ForeignKey('airport.id'), unique=False)
    destino = Column(ForeignKey('airport.id'), unique=False)
    assDisp = Column(Integer, unique=False)
    hora = Column(DateTime, unique=False)
    tarifa = Column(Float, unique=False)

    def __init__(self, origem, destino=None, assDisp=None, hora=None, tarifa=None):
        self.origem = origem
        self.destino = destino
        self.assDisp = assDisp
        self.hora = hora
        self.tarifa = tarifa

class Reserve(Base):
    __tablename__ = 'reserve'
    id = Column(Integer, primary_key=True)
    voo = Column(ForeignKey('flight.id'), unique=False)
    eticket = Column(Integer, unique=True)

    def __init__(self, voo=None, eticket=None):
        self.voo = voo
        self.eticket = eticket