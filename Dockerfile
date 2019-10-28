FROM registry.es.gov.br/espm/infraestrutura/containers/python:3.6.9

RUN mkdir app

COPY . /app

RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev -y

RUN pip3 install -r app/requirements.txt

WORKDIR /app/sedu_webservice/
CMD ["python3", "manage.py", "runserver"]