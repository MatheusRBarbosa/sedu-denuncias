FROM registry.es.gov.br/espm/infraestrutura/containers/python-mssql:latest

RUN mkdir app

COPY . /app

RUN apt-get update

RUN pip3 install -r app/requirements.txt

EXPOSE 8000

WORKDIR /app/sedu_webservice/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]