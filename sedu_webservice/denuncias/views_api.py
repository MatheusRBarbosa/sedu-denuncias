from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

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

    def create_aluno(self, request):
        aluno_data = {}
        aluno_data['nome']= request.data.get('aluno')
        aluno_data['cod_energia']= request.data.get('codigo_edp')
        aluno_data['escola'] = Escola.objects.get(cod_inep=request.data.get('inep_escola'))            
        aluno = Aluno(**aluno_data)
        aluno.save()
        return aluno

    def upsert_reclamante(self, request):
        nome = request.data.get('autor')
        email = request.data.get('email')
        reclamante = Reclamante.objects.get_or_create(nome=nome, email=email)
        return reclamante
        
    def post(self, request, format=None):
        serializer = ReclamacaoAPISerializer(data=request.data)
        if serializer.is_valid():
            aluno = self.create_aluno(request)       

            # Retorna um tupla (object, boolean)
            # object = Objeto do banco
            # boolean = True se foi criado e False se tiver sido retornado do banco
            reclamante = self.upsert_reclamante(request)
            
            reclamacao_data = {}
            reclamacao_data['aluno'] = aluno
            reclamacao_data['texto'] = request.data.get('descricao')
            # agencia
            reclamacao_data['reclamante'] = reclamante[0]
            # cod_linha
            reclamacao_data['tipo'] = TipoReclamacao.objects.get(pk=request.data.get('tipo_reclamacao'))
            reclamacao_data['data_ocorrido'] = request.data.get('data_ocorrido')
            reclamacao = Reclamacao(**reclamacao_data)
            reclamacao.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get_extra_actions(cls):
        return []

