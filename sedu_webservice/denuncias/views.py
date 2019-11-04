from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class SuperintendenciaViewSet(viewsets.ModelViewSet):
    queryset = Superintendencia.objects.all()
    serializer_class = SuperintendenciaSerializer

class SREViewSet(viewsets.ModelViewSet):
    queryset = SRE.objects.all()
    serializer_class = SRESerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class AgenciaTransporteViewSet(viewsets.ModelViewSet):
    queryset = AgenciaTransporte.objects.all()
    serializer_class = AgenciaTransporteSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ReclamanteViewSet(viewsets.ModelViewSet):
    queryset = Reclamante.objects.all()
    serializer_class = ReclamanteSerializer

class ReclamacaoStatusViewSet(viewsets.ModelViewSet):
    queryset = ReclamacaoStatus.objects.all()
    serializer_class = ReclamacaoStatusSerializer

class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

