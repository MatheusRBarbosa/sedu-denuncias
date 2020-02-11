FROM registry.es.gov.br/espm/infraestrutura/containers/python:3.6.9

RUN mkdir app

COPY . /app

RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev -y
RUN apt-get install unixodbc unixodbc-dev -y


RUN pip3 install -r app/requirements.txt

EXPOSE 8000

WORKDIR /app/sedu_webservice/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]