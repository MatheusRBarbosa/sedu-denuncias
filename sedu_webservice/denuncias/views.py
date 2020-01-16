from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView, DetailView, View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect

##Paginas Web
@method_decorator(login_required, name='dispatch')
class ReclamacaoList(ListView):
    
    def renderPage(request):
        userGroups = request.user.groups.all()
        groupsList = []
        
        for g in userGroups:
            groupsList.append(g.name.upper())

        if(len(groupsList) == 0 or 'SEDU' in groupsList):
            reclamacoes = Reclamacao.objects.all()
        else:
            reclamacoes = Reclamacao.objects.filter(sre_responsavel__in=userGroups)

        return render(request, 'denuncias/reclamacao_list.html', {'reclamacoes': reclamacoes})

@method_decorator(login_required, name='dispatch')
class ReclamacaoDetail(UpdateView): 
    model = Reclamacao
    fields = '__all__'
    template_name = 'denuncias/reclamacao_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReclamacaoDetail, self).get_context_data(**kwargs)
        reclamacao = context['reclamacao']
        sre = SRE.objects.get(pk=reclamacao.sre_responsavel)
        print(sre)
        userGroups = self.request.user.groups.all()
        can_view = False

        for g in userGroups:
            if(g.name == sre.name or g.name.upper() == 'SEDU'):
                can_view = True

        if (len(userGroups) == 0):
            can_view = True
            
        context['can_view'] = can_view
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        Reclamacao.objects.filter(pk=self.kwargs['pk']).update(status=request.POST.get("status"))
        return redirect('web_reclamacao_detail', self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class ReclamacaoCreate(CreateView): 
    model = Reclamacao
    fields = '__all__'
    success_url = reverse_lazy('web_reclamacao_list')

    def load_rotas(request):
        aluno_id = request.GET.get('alunoId')
        aluno = Aluno.objects.get(pk=aluno_id)
        rotas = Rota.objects.filter(escola=aluno.escola)
        return render(request, 'denuncias/ajax/rotas.html', {'rotas': rotas})

    def get_context_data(self, *args, **kwargs):
        context = super(ReclamacaoCreate, self).get_context_data(**kwargs)
        
        userGroup = self.request.user.groups.all()
        groupsList = []
        
        for g in userGroup:
            groupsList.append(g.name.upper())

        if(len(groupsList) == 0 or 'SEDU' in groupsList):
            context['alunos'] = Aluno.objects.all()
        else:
            context['alunos'] = Aluno.objects.filter(escola__municipio__sre__in=userGroup)
            
        context['rotas'] = None
        return context

    def post(self, request, *args, **kwargs):
        reclamacao_data = {}
        aluno = Aluno.objects.get(id=request.POST.get('aluno'))
        reclamacao_data['aluno'] = aluno
        reclamacao_data['reclamante'] = Reclamante.objects.get(id=request.POST.get('reclamante'))
        reclamacao_data['agencia_transporte'] = AgenciaTransporte.objects.get(id=request.POST.get('agencia_transporte'))
        reclamacao_data['tipo'] = TipoReclamacao.objects.get(id=request.POST.get('tipo'))
        reclamacao_data['data_ocorrido'] = request.POST.get('data_ocorrido')
        reclamacao_data['texto'] = request.POST.get('texto')
        reclamacao_data['rota'] = Rota.objects.get(id=request.POST.get('rota'))
        reclamacao_data['papel'] = Papel.objects.get(id=request.POST.get('papel'))
        reclamacao_data['outro_papel'] = request.POST.get('outro_papel')
        reclamacao_data['placa_veiculo'] = request.POST.get('placa_veiculo')

        reclamacao_data['sre_responsavel'] = aluno.escola.municipio.sre
        reclamacao_data['status'] = ReclamacaoStatus.objects.get(id=1)
        reclamacao = Reclamacao(**reclamacao_data)
        reclamacao.save()

        return redirect('web_reclamacao_list')

@method_decorator(login_required, name='dispatch')
class ComentarioCreate(CreateView): 
    model = Comentario
    fields = '__all__'
    template_name = 'denuncias/comentario_form.html'

    def get_context_data(self, *args, **kwargs):
       context = super(ComentarioCreate, self).get_context_data(**kwargs)
       context['reclamacao'] = Reclamacao.objects.get(id=self.kwargs['pk'])
       full_name = self.request.user.first_name + ' ' + self.request.user.last_name
       context['responsavel'] = full_name
       
       return context

    def post(self, request, *args, **kwargs):
        reclamacao = Reclamacao.objects.get(id=self.kwargs['pk'])
        try:
            resp = Responsavel.objects.get(usuario=request.user.id)
        except:
            if(request.user.username == "admin"):
                resp = Responsavel(usuario=request.user, sre=reclamacao.aluno.escola.municipio.sre)
                resp.save()
        
        comentario_data = {}
        comentario_data['texto'] = request.POST.get('texto')
        comentario_data['reclamacao'] = reclamacao
        comentario_data['responsavel'] = resp
        comentario = Comentario(**comentario_data)
        comentario.save()

        reclamacao.status = ReclamacaoStatus.objects.get(nome="Analisando")
        reclamacao.save()

        return redirect('web_reclamacao_detail', self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class ParecerFinalCreate(CreateView):
    model = Comentario
    fields = '__all__'
    template_name = 'denuncias/parecerFinal_form.html'
    
    def get_context_data(self, *args, **kwargs):
       context = super(ParecerFinalCreate, self).get_context_data(**kwargs)
       context['reclamacao'] = Reclamacao.objects.get(id=self.kwargs['pk'])
       full_name = self.request.user.first_name + ' ' + self.request.user.last_name
       context['responsavel'] = full_name
       
       return context
    
    def post(self, request, *args, **kwargs):
        reclamacao = Reclamacao.objects.get(id=self.kwargs['pk'])
        
        try:
            resp = Responsavel.objects.get(usuario=request.user.id)
        except:
            if(request.user.username == "admin"):
                resp = Responsavel(usuario=request.user, sre=reclamacao.aluno.escola.municipio.sre)
                resp.save()
        
        parecer_data = {}
        parecer_data['texto'] = request.POST.get('texto')
        parecer_data['reclamacao'] = reclamacao
        parecer_data['responsavel'] = resp
        parecer = ParecerFinal(**parecer_data)
        parecer.save()

        reclamacao.status = ReclamacaoStatus.objects.get(nome="Concluído")
        reclamacao.save()
        return redirect('web_reclamacao_detail', self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class AlunoCreate(CreateView):
    model = Aluno
    fields = '__all__'
    template_name = 'denuncias/aluno_form.html'

    def load_municipios(request):
        sreId = request.GET.get('id')
        sre = SRE.objects.get(pk=sreId)
        municipios = Municipio.objects.filter(sre=sre)
        return render(request, 'denuncias/ajax/municipios.html', {'municipios': municipios})

    def load_escolas(request):
        municipioId = request.GET.get('id')
        municipio = Municipio.objects.get(pk=municipioId)
        escolas = Escola.objects.filter(municipio=municipio)
        return render(request, 'denuncias/ajax/escolas.html', {'escolas': escolas})

    def get_context_data(self, *args, **kwargs):
       context = super(AlunoCreate, self).get_context_data(**kwargs)
       userGroups = self.request.user.groups.all()
       context['sres'] = SRE.objects.filter(pk__in=userGroups)
       return context

    def post(self, request, *args, **kwargs):

        aluno_data = {}
        aluno_data['nome'] = request.POST.get('nome')
        aluno_data['ra'] = request.POST.get('ra')
        aluno_data['cod_energia'] = request.POST.get('cod_energia')
        aluno_data['escola'] = Escola.objects.get(pk=request.POST.get('escola'))
        
        isReclamante = request.POST.get('isReclamante')

        aluno = Aluno(**aluno_data)
        aluno.save()
        if(isReclamante == 'on'):
            try:
                reclamante = Reclamante.objects.get(email=request.POST.get('email'))
                reclamante.nome = aluno_data['nome']
            except:
                reclamante = Reclamante(nome=aluno_data['nome'], email=request.POST.get('email'))
            reclamante.save()
        
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class ReclamanteCreate(CreateView):
    model = Reclamante
    fields = '__all__'
    template_name = 'denuncias/reclamante_form.html'
    
    def post(self, request, *args, **kwargs):
        reclamante_data = {}
        reclamante_data['nome'] = request.POST.get('nome')
        reclamante_data['email'] = request.POST.get('email')

        try:
            reclamante = Reclamante.objects.get(email=reclamante_data['email'])
            reclamante.nome = reclamante_data['nome']
        except:
            reclamante = Reclamante(**reclamante_data)
        reclamante.save()
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class Encaminhar(CreateView):
    model = Comentario
    fields = '__all__'
    template_name = 'denuncias/encaminhar_form.html'
    
    def get_context_data(self, *args, **kwargs):
       context = super(Encaminhar, self).get_context_data(**kwargs)
       context['reclamacao'] = Reclamacao.objects.get(id=self.kwargs['pk'])
       full_name = self.request.user.first_name + ' ' + self.request.user.last_name
       context['responsavel'] = full_name
       context['sres'] = SRE.objects.all()
       
       return context
    
    def post(self, request, *args, **kwargs):
        reclamacao = Reclamacao.objects.get(id=self.kwargs['pk'])
        sre_id = request.POST.get('sre')

        reclamacao.status = ReclamacaoStatus.objects.get(nome="Encaminhado")
        reclamacao.sre_responsavel = SRE.objects.get(pk=sre_id)
        reclamacao.save()
        return redirect('web_reclamacao_list')