from rest_framework import routers
from .views import *
from django.urls import path

router = routers.SimpleRouter()

router.register(r'superintendencias', SuperintendenciaViewSet)
router.register(r'sres', SREViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'escolas', EscolaViewSet)
router.register(r'agencias_transporte', AgenciaTransporteViewSet)
router.register(r'alunos', Aluno_ViewSet)
router.register(r'reclamantes', Reclamante_ViewSet)
router.register(r'reclamacao_status', ReclamacaoStatusViewSet)
router.register(r'reclamacoes', ReclamacaoViewSet)
router.register(r'responsaveis', ResponsavelViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = router.urls