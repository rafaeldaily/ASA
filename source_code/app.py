# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016
  #Teste

from flask import Flask
from routes import urls_blueprint
import database


app = Flask(__name__)
# register routes from urls
app.register_blueprint(urls_blueprint)
database.init_db()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
