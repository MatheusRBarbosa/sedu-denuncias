from rest_framework import routers
from .views_api import *
from django.urls import path

router = routers.SimpleRouter()

router.register(r'sres', SREViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'escolas', EscolaViewSet)
router.register(r'agencias_transporte', AgenciaTransporteViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'reclamantes', ReclamanteViewSet)
router.register(r'reclamacao_status', ReclamacaoStatusViewSet)
router.register(r'reclamacoes', ReclamacaoViewSet)
router.register(r'responsaveis', ResponsavelViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'tipo_reclamacao', TipoReclamacaoViewSet)

urlpatterns = router.urls