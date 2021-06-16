# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016

# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")