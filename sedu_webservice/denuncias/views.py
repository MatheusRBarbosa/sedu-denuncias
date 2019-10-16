from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class Superintendencia_ViewSet(viewsets.ModelViewSet):
    queryset = Superintendencia.objects.all()
    serializer_class = Superintendencia_Serializer

class SRE_ViewSet(viewsets.ModelViewSet):
    queryset = SRE.objects.all()
    serializer_class = SRE_Serializer

class Municipio_ViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = Municipio_Serializer

class Escola_ViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = Escola_Serializer

class Agencia_Transporte_ViewSet(viewsets.ModelViewSet):
    queryset = Agencia_Transporte.objects.all()
    serializer_class = Agencia_Transporte_Serializer

class Aluno_ViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = Aluno_Serializer

class Reclamante_ViewSet(viewsets.ModelViewSet):
    queryset = Reclamante.objects.all()
    serializer_class = Reclamante_Serializer

class Reclamacao_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao_Status.objects.all()
    serializer_class = Reclamacao_Status_Serializer

class Reclamacao_ViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = Reclamacao_Serializer

class Responsavel_ViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = Responsavel_Serializer

class Comentario_ViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = Comentario_Serializer

