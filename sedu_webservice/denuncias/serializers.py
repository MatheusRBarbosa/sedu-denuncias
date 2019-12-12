from rest_framework import serializers
from .models import *

class SRESerializer(serializers.ModelSerializer):

    class Meta:
        model = SRE
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = '__all__'

class EscolaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Escola
        fields = '__all__'

class AgenciaTransporteSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgenciaTransporte
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'

class ReclamanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamante
        fields = '__all__'

class ReclamacaoStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReclamacaoStatus
        fields = '__all__'

class TipoReclamacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoReclamacao
        fields = '__all__'
class ReclamacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamacao
        fields = '__all__'

class ResponsavelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsavel
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = '__all__'

class ReclamacaoAPISerializer(serializers.Serializer):

    autor = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    aluno = serializers.CharField(max_length=255)
    codigo_edp = serializers.CharField(max_length=255)
    tipo_reclamacao = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    inep_escola = serializers.CharField(max_length=255)
    data_ocorrido = serializers.DateTimeField()

