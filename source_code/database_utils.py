# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016

from models import Airport, Flight, Reserve
from sqlalchemy import update
from random import *
import database

def add_airports(aeroporto_data):
    db = database.SessionLocal()
    aeroporto = Airport(aeroporto_data['nome'])
    print(aeroporto)
    db.add(aeroporto)
    db.commit()
    db.close()

def get_airports():
    db = database.SessionLocal()
    aeroporto = Airport.query.all()
    #aeroporto2 = Airport.query. 
    print(aeroporto)
    db.close()
    if aeroporto:
        return aeroporto
    else:
        return None

def get_airports_origem(origem):
    db = database.SessionLocal()
    id_or = int(origem['origem'])
    aeroporto = []
    voos = Flight.query.all()

    for voo in voos:
        if voo.origem == id_or:
            aeroporto.append(db.query(Airport).filter_by(id=voo.destino).first())

    #aeroporto2 = Airport.query. 
    print(aeroporto)
    db.close()
    if aeroporto:
        return aeroporto
    else:
        return None



def get_flights(horario):
    db = database.SessionLocal()
    #hora = voos_data['hora']
    voos = Flight.query.filter_by(hora=horario['hora'])
    #aeroporto2 = Airport.query. 
    print(voos)
    db.close()
    if voos:
        return voos
    else:
        return None


def add_flights(voo_data):
    db = database.SessionLocal()
    voo = Flight(voo_data['origem'], voo_data['destino'], voo_data['assDisp'], voo_data['hora'], voo_data['tarifa'])
    print(voo)
    db.add(voo)
    db.commit()
    db.close()


def get_pesquisa(passageiros):
    db = database.SessionLocal()
    #hora = voos_data['hora']
    voos = Flight.query.order_by(Flight.tarifa).all()
    voos2 = []
    for voo in voos:
        if voo.assDisp >= int(passageiros['passageiros']):
            voos2.append(voo)
    #aeroporto2 = Airport.query. 
    print(voos2)
    db.close()
    if voos2:
        return voos2
    else:
        return None


def add_reserva(id_voo):
    db = database.SessionLocal()
    voo = Flight.query.filter_by(id=int(id_voo['voo'])).first()
    voo.assDisp = voo.assDisp - 1
    reserva = Reserve(int(id_voo['voo']), randrange(1000))
    db.add(reserva)
    db.commit()
    res={'localizador': reserva.id, 'eticket': reserva.eticket}
    db.close()
    return res