from rest_framework import routers
from .views import *
from django.urls import path

urlpatterns = [
    path('reclamacoes/', ReclamacaoList.renderPage, name='web_reclamacao_list'),
    path('reclamacao/<int:pk>', ReclamacaoDetail.as_view(), name='web_reclamacao_detail'),
    path('reclamacao_create', ReclamacaoCreate.as_view(), name='web_reclamacao_create'),
    path('reclamacao/<int:pk>/comentario_create', ComentarioCreate.as_view(), name='web_comentario_create'),
    path('reclamacao/<int:pk>/parecer_final_create', ParecerFinalCreate.as_view(), name='web_parecer_final'),
    path('aluno_create', AlunoCreate.as_view(), name='web_aluno_create'),
    path('reclamante_create', ReclamanteCreate.as_view(), name='web_reclamante_create'),
    path('ajax/load-rotas', ReclamacaoCreate.load_rotas, name='ajax_load_rotas'),
]