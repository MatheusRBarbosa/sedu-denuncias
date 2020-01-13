from rest_framework import serializers
from .models import *

class ReclamacaoAPISerializer(serializers.Serializer):

    autor = serializers.CharField(max_length=255)
    acesso_cidadao = serializers.UUIDField()
    papelDoAutor = serializers.IntegerField()
    email = serializers.EmailField(max_length=255)
    aluno = serializers.CharField(max_length=255)
    registroAcademico = serializers.CharField(max_length=255)
    codigoEDP = serializers.CharField(max_length=255)
    escolaId = serializers.IntegerField()
    placaVeiculo = serializers.CharField(max_length=255)
    rotaId = serializers.IntegerField()
    tipoReclamacao = serializers.IntegerField()
    dataReclamacao = serializers.DateTimeField()
    descricao = serializers.CharField(max_length=255)
    protocolo = serializers.CharField(max_length=255, required=False)
