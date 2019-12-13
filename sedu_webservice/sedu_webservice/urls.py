from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import TemplateView
import os

schema_view = get_schema_view(
   openapi.Info(
      title="SEDU: Denuncias de Transporte API",
      default_version='v1',
      description="API para registrar as denuncias de transporte da SEU",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

if (os.getenv('PATH_PRODUCTION') == 'sedu'):
   urlpatterns = [
      path('sedu/api/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      path('sedu/api/docs/?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
      path('sedu/admin/', admin.site.urls),
      path('sedu/web/', include('denuncias.urls')),

      path('sedu/api/auth/', include('rest_framework.urls')),
      path('sedu/api/denuncias/', include('denuncias.urls_api')),
      path('sedu/accounts/', include('django.contrib.auth.urls')),
      path('sedu', TemplateView.as_view(template_name='home.html'), name='home'),

   ]
else:
   urlpatterns = [
      path('api/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      path('api/docs/?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
      path('admin/', admin.site.urls),
      path('web/', include('denuncias.urls')),

      path('api/auth/', include('rest_framework.urls')),
      path('api/denuncias/', include('denuncias.urls_api')),
      path('accounts/', include('django.contrib.auth.urls')),
      path('', TemplateView.as_view(template_name='home.html'), name='home'),

   ]
