from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import HttpResponse, JsonResponse

class MunicipioAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            municipios = Municipio.objects.all()

            response.append(serializers.serialize("json", municipios))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class EscolaAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            escolas = Escola.objects.all()

            response.append(serializers.serialize("json", escolas))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class TiposReclamacaoAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            tipos = TipoReclamacao.objects.all()

            response.append(serializers.serialize("json", tipos))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class PapelAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            papeis = Papel.objects.all()

            response.append(serializers.serialize("json", papeis))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class TurnoAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            turnos = Turno.objects.all()

            response.append(serializers.serialize("json", turnos))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class StatusAPIViewSet(APIView):
    def get(self, request, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            status = ReclamacaoStatus.objects.all()

            response.append(serializers.serialize("json", status))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class ReclamacaoAPIViewSet(APIView):

    def create_aluno(self, request):
        aluno_data = {}
        aluno_data['nome']= request.data.get('aluno')
        aluno_data['cod_energia']= request.data.get('codigoEDP')
        aluno_data['escola'] = Escola.objects.get(pk=request.data.get('escolaId'))            
        aluno = Aluno(**aluno_data)
        aluno.save()
        return aluno

    def upsert_reclamante(self, request):
        
        nome = request.data.get('autor')
        email = request.data.get('email')
        sub_novo = request.data.get('acesso_cidadao')
        
        try:
            reclamante = Reclamante.objects.get(sub_novo=sub_novo)
        except:
            reclamante = Reclamante(nome=nome, email=email, sub_novo=sub_novo)
            reclamante.save()
        return reclamante
        
    def post(self, request, format=None):
        
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            
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
                reclamacao_data['reclamante'] = reclamante
                reclamacao_data['tipo'] = TipoReclamacao.objects.get(pk=request.data.get('tipoReclamacao'))
                reclamacao_data['outro_tipo'] = request.data.get('outroTipo')
                reclamacao_data['data_ocorrido'] = request.data.get('dataReclamacao')
                reclamacao_data['placa_veiculo'] = request.data.get('placaVeiculo')
                reclamacao_data['rota'] = Rota.objects.get(pk=request.data.get('rotaId'))
                reclamacao_data['papel'] = Papel.objects.get(pk=request.data.get('papelDoAutor'))
                reclamacao_data['outro_papel'] = request.data.get('outroPapel')
                escola =  Escola.objects.get(pk=request.data.get('escolaId'))
                reclamacao_data['sre_responsavel'] = escola.municipio.sre

                reclamacao = Reclamacao(**reclamacao_data)
                reclamacao.save()

                # Eh necessario fazer uma consulta pois o protocolo eh gerado depois do save
                r = Reclamacao.objects.get(pk=reclamacao.id)
                return Response(r.protocolo, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return HttpResponse("Token de autenticação inválido.")

class ReclamanteAPIViewSet(APIView):
    def get(self, request, pk, format=None):
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            reclamacoes = []
            reclamante = Reclamante.objects.filter(sub_novo=pk)

            if (reclamante.count() > 0):
                reclamacoes = Reclamacao.objects.filter(reclamante__in=reclamante)

            response.append(serializers.serialize("json", reclamacoes))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")


class RotasEscolaAPIViewSet(APIView):
    def get(self, request, pk, format=None):

        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            rotas = Rota.objects.filter(escola=pk)

            response.append(serializers.serialize("json", rotas))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")

class ParecerFinalAPIViewSet(APIView):
    def get(self, request, pk, format=None):
        
        try:
            key = Token.objects.get(key=request.META.get('HTTP_TOKEN'))
            response = []
            parecer = ParecerFinal.objects.filter(reclamacao=pk)

            response.append(serializers.serialize("json", parecer))
            return HttpResponse(response)
        except:
            return HttpResponse("Token de autenticação inválido.")
