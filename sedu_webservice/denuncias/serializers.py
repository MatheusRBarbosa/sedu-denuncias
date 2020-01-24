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

class ParecerFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParecerFinal
        fields = ['texto']

class AlunoSerializer(serializers.ModelSerializer):

    escola = serializers.StringRelatedField()

    class Meta:
        model = Aluno
        fields = ('nome', 'cod_energia', 'ra', 'escola')

class ReclamanteSerializer(serializers.ModelSerializer):
    papel = serializers.StringRelatedField()
    aluno = AlunoSerializer(read_only=True)
    rota = serializers.StringRelatedField()
    reclamante = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    tipo = serializers.StringRelatedField()
    #parecerFinal = ParecerFinalSerializer(read_only=True)
 
    class Meta:
        model = Reclamacao
        fields = ('pk', 'aluno', 'texto', 'papel', 'outro_papel', 'agencia_transporte', 'reclamante', 'protocolo', 'status', 'data_ocorrido', 'rota', 'placa_veiculo', 'tipo', 'outro_tipo', 'sre_responsavel', 'created_on')