from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView

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

class TipoReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = TipoReclamacao.objects.all()
    serializer_class = TipoReclamacaoSerializer

class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ReclamacaoAPIViewSet(APIView):
    queryset = Comentario.objects.all()
    def post(self, request, format=None):
        serializer = ReclamacaoAPISerializer(data=request.data)
        if serializer.is_valid():
            aluno_data = {}
            aluno_data['nome']= request.data.get('aluno')
            aluno_data['cod_energia']= request.data.get('codigoedp')

            aluno = Aluno(**aluno_data)
            #aluno.save()
            print(aluno)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_extra_actions(cls):
        return []

