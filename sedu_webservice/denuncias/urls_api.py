from rest_framework import routers
from .views_api import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

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
router.register(r'turno', TurnoViewSet)
#router.register(r'mensagem', ReclamacaoAPIViewSet.as_view(), base_name='mensagem')

urlpatterns = [
    path('reclamacao', ReclamacaoAPIViewSet.as_view()),
    path('reclamante/<int:pk>/reclamacoes', ReclamanteAPIViewSet.get),
    path('escola/<int:pk>/rotas', RotasEscolaAPIViewSet.get)
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
