from rest_framework import routers
from .views import *
from django.urls import path

urlpatterns = [
    path('reclamacoes/', ReclamacaoList.as_view(), name='web_reclamacao_list'),
    path('reclamacao/<int:pk>', ReclamacaoDetail.as_view(), name='web_reclamacao_detail'),
    path('reclamacao_create', ReclamacaoCreate.as_view(), name='web_reclamacao_create'),
    path('reclamacao_update/<int:pk>', ReclamacaoUpdate.as_view(), name='web_reclamacao_update'),
    path('reclamacao_delete/<int:pk>', ReclamacaoDelete.as_view(), name='web_reclamacao_delete'),
]