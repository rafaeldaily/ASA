# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016

from sqlalchemy.sql.expression import null, true
from models import Airport, Flight, Reserve
import database_utils
import database
from flask import Blueprint, request, json, jsonify

urls_blueprint = Blueprint('urls', __name__,)

login = False

@urls_blueprint.route('/')
def index():
    global login
    print(login)
    if login:
        return 'urls index route'
    else:
        return 'Faca o Login'


@urls_blueprint.route('/login', methods = ['POST'])
def loginAPI():
    global login
    user = "admin"
    senha = "admin"
    login_data = request.get_json()
    if login_data['user'] == user and login_data['senha'] == senha:
        login = True
        return "Login realizado"
    else:
        return "user e/ou senha errados"

@urls_blueprint.route('/logout', methods = ['GET'])
def logoutAPI():
    global login
    login=False
    return "logout realizado com sucesso"


###############################################################################################################################


#(ex 4)
@urls_blueprint.route('/airports', methods = ['GET'])
def get_airports():
    global login
    if login:   
        all_aeroportos = database_utils.get_airports()
        all_aeroportos_array_json = []
        for aeroporto in all_aeroportos:
            aeroporto_json = {"nome": aeroporto.nome}
            all_aeroportos_array_json.append(aeroporto_json)
            print(aeroporto.nome)
        return json.dumps(all_aeroportos_array_json)
    else:
        return 'Faca o Login'

@urls_blueprint.route('/airports', methods = ['POST'])
def add_airports():
    global login
    if login:
        aeroportos_data = request.get_json()
        #print(aeroportos_data)
        database_utils.add_airports(aeroportos_data)
        return 'Aeroporto adicionado'
    else:
        return 'Faca o Login'

#5
@urls_blueprint.route('/airports/origem', methods = ['GET'])
def get_airports_origem():
    global login
    if login:   
        aeroportos_data = request.get_json()
        all_aeroportos = database_utils.get_airports_origem(aeroportos_data)
        all_aeroportos_array_json = []
        if all_aeroportos:

            for aeroporto in all_aeroportos:
                aeroporto_json = {"nome": aeroporto.nome}
                all_aeroportos_array_json.append(aeroporto_json)
                print(aeroporto.nome)
        else:
            return json.dumps(all_aeroportos)
        return json.dumps(all_aeroportos_array_json)
    else:
        return 'Faca o Login'


@urls_blueprint.route('/flights', methods = ['GET'])
def get_flights():
    global login
    if login:
        voos_data = request.get_json()
        all_voos = database_utils.get_flights(voos_data)
        all_voos_array_json = []
        for voo in all_voos:
            voo_json = {"origem": voo.origem, "destino": voo.destino, "assDisp": voo.assDisp, "hora": voo.hora, "tarifa": voo.tarifa}
            all_voos_array_json.append(voo_json)
            print(voo.origem)
        return json.dumps(all_voos_array_json)
    else:
        return 'Faca o Login'

@urls_blueprint.route('/flights', methods = ['POST'])
def add_flights():
    global login
    if login:
        flights_data = request.get_json()
        #print(aeroportos_data)
        database_utils.add_flights(flights_data)
        return 'flight adicionado'
    else:
        return 'Faca o Login'

#7
@urls_blueprint.route('/flights/pesquisa', methods = ['GET'])
def get_pesquisa():
    global login
    if login:
        voos_data = request.get_json()
        all_voos = database_utils.get_pesquisa(voos_data)
        all_voos_array_json = []
        if all_voos:
            for voo in all_voos:
                voo_json = {"origem": voo.origem, "destino": voo.destino, "assDisp": voo.assDisp, "hora": voo.hora, "tarifa": voo.tarifa}
                all_voos_array_json.append(voo_json)
                print(voo)
        else:
            return all_voos
        return json.dumps(all_voos_array_json)
    else:
        return 'Faca o Login'


#8
@urls_blueprint.route('/comprar', methods = ['POST'])
def add_reserva():
    global login
    if login:
        voos_data = request.get_json()
        return database_utils.add_reserva(voos_data)
    else:
        return 'Faca o Login'