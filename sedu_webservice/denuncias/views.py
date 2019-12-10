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
    #queryset = Reclamacao.objects.all()
    
    def renderPage(request):
        userGroups = request.user.groups.all()
        groupsList = []
        
        for g in userGroups:
            groupsList.append(g.name)

        if(len(groupsList) == 0):
            reclamacoes = Reclamacao.objects.all()
        else:
            reclamacoes = Reclamacao.objects.filter(aluno__escola__municipio__sre__in=userGroups)

        return render(request, 'denuncias/reclamacao_list.html', {'reclamacoes': reclamacoes})

@method_decorator(login_required, name='dispatch')
class ReclamacaoDetail(UpdateView): 
    model = Reclamacao
    fields = '__all__'
    template_name = 'denuncias/reclamacao_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReclamacaoDetail, self).get_context_data(**kwargs)
        reclamacao = context['reclamacao']
        sre_reclamacao = reclamacao.aluno.escola.municipio.sre
        
        userGroups = self.request.user.groups.all()
        can_view = False

        for g in userGroups:
            if(g.name == sre_reclamacao.name):
                can_view = True

        if (len(userGroups) == 0):
            can_view = True
            
        context['can_view'] = can_view
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        Reclamacao.objects.filter(pk=self.kwargs['pk']).update(status=request.POST.get("status"))
        return redirect('web_reclamacao_list')

@method_decorator(login_required, name='dispatch')
class ReclamacaoCreate(CreateView): 
    model = Reclamacao
    fields = '__all__'
    success_url = reverse_lazy('web_reclamacao_list')

class ComentarioCreate(CreateView): 
    model = Comentario
    fields = '__all__'
    template_name = 'denuncias/comentario_form.html'
    success_url = reverse_lazy('web_reclamacao_list')

    def get_context_data(self, *args, **kwargs):
       context = super(ComentarioCreate, self).get_context_data(**kwargs)
       reclamacao = Reclamacao.objects.get(id=self.kwargs['pk'])
       context['protocolo'] = reclamacao.protocolo
       full_name = self.request.user.first_name + ' ' + self.request.user.last_name
       context['responsavel'] = full_name
       
       return context

    def post(self, request, *args, **kwargs):
        resp = Responsavel.objects.get(usuario=request.user.id)
        reclamacao = Reclamacao.objects.get(id=self.kwargs['pk'])
        comentario_data = {}
        comentario_data['texto'] = request.POST.get('texto')
        comentario_data['reclamacao'] = reclamacao
        comentario_data['responsavel'] = resp
        comentario = Comentario(**comentario_data)
        comentario.save()

        return redirect('web_reclamacao_detail', self.kwargs['pk'])
