# Alunos:
  #Nome : Rafael Daily Santos Martins
  #Matrícula : 12011ECP027

  #Nome : Leonardo Cauhi Salomão
  #Matrícula : 12011ECP016

FROM python:3.7

RUN apt-get update && apt-get install python-pip -y && apt-get install python-dev -y
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]