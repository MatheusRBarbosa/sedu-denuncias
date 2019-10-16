from rest_framework import serializers
from .models import *

class Superintendencia_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Superintendencia
        fields = '__all__'

class SRE_Serializer(serializers.ModelSerializer):

    class Meta:
        model = SRE
        fields = '__all__'

class Municipio_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = '__all__'

class Escola_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Escola
        fields = '__all__'

class Agencia_Transporte_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Agencia_Transporte
        fields = '__all__'

class Aluno_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'

class Reclamante_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamante
        fields = '__all__'

class Reclamacao_Status_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamacao_Status
        fields = '__all__'

class Reclamacao_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamacao
        fields = '__all__'

class Responsavel_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Responsavel
        fields = '__all__'

class Comentario_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = '__all__'

