from rest_framework import routers
from .views import *
from django.urls import path

router = routers.SimpleRouter()

router.register(r'superintendencias', Superintendencia_ViewSet)
router.register(r'sres', SRE_ViewSet)
router.register(r'municipios', Municipio_ViewSet)
router.register(r'escolas', Escola_ViewSet)
router.register(r'agencias_transporte', Agencia_Transporte_ViewSet)
router.register(r'alunos', Aluno_ViewSet)
router.register(r'reclamantes', Reclamante_ViewSet)
router.register(r'reclamacao_status', Reclamacao_Status_ViewSet)
router.register(r'reclamacoes', Reclamacao_ViewSet)
router.register(r'responsaveis', Responsavel_ViewSet)
router.register(r'comentarios', Comentario_ViewSet)

urlpatterns = router.urls