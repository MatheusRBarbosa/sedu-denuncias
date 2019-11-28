from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

##Paginas Web
@method_decorator(login_required, name='dispatch')
class ReclamacaoList(ListView):
    #model = Reclamacao
    context_object_name = 'reclamacoes'
    queryset = Reclamacao.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReclamacaoList, self).get_context_data(**kwargs)
        context['reclamacoes'] = self.queryset
        context['SREs'] = SRE.objects.all()
        context['tipos'] = TipoReclamacao.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ReclamacaoDetail(DetailView): 
    model = Reclamacao
    
@method_decorator(login_required, name='dispatch')
class ReclamacaoCreate(CreateView): 
    model = Reclamacao
    fields = '__all__'
    success_url = reverse_lazy('web_reclamacao_list')

@method_decorator(login_required, name='dispatch')
class ReclamacaoUpdate(UpdateView): 
    model = Reclamacao
    fields = '__all__'
    success_url = reverse_lazy('web_reclamacao_list')

@method_decorator(login_required, name='dispatch')
class ReclamacaoDelete(DeleteView): 
    model = Reclamacao
    success_url = reverse_lazy('web_reclamacao_list')
