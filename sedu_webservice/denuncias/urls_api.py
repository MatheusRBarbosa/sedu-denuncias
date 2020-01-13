from rest_framework import routers
from .views_api import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()

urlpatterns = [
    path('reclamacao', ReclamacaoAPIViewSet.as_view()),
    path('reclamante/<uuid:pk>/reclamacoes', ReclamanteAPIViewSet.as_view()),
    path('escola/<int:pk>/rotas', RotasEscolaAPIViewSet.as_view()),
    path('municipios', MunicipioAPIViewSet.as_view()),
    path('escolas', EscolaAPIViewSet.as_view()),
    path('tipos', TiposReclamacaoAPIViewSet.as_view()),
    path('reclamante/papeis', PapelAPIViewSet.as_view()),
    path('rotas/turnos', TurnoAPIViewSet.as_view()),
    path('reclamacao/status', StatusAPIViewSet.as_view()),
    path('reclamacao/<int:pk>/parecer', ParecerFinalAPIViewSet.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
