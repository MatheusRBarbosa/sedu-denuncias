from django.contrib import admin
from .models import *
# Register your models here.

class ReclamacaoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('aluno','protocolo','agencia_transporte','municipio', 'reclamante', 'status')
    list_filter = ('agencia_transporte','municipio', 'status')
    search_fields = (['protocolo', 'aluno'])

class AlunoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('nome','ra','cod_energia','escola')
    list_filter = (['escola'])
    search_fields = (['nome','ra','cod_energia'])

class AgenciaTransporteAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    list_filter = ('nome','sre','superintendencia')
    search_fields = (['nome'])

class EscolaAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome', 'municipio'])
    list_filter = (['municipio'])
    search_fields = (['nome'])

class MunicipioAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome', 'superintendencia'])
    list_filter = (['superintendencia'])
    search_fields = (['nome'])

class ReclamanteAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    list_filter = ([])
    search_fields = (['nome'])

class ResponsavelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['usuario','superintendencia'])
    list_filter = (['superintendencia'])
    search_fields = (['usuario'])

class SreAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    list_filter = ([])
    search_fields = (['nome'])


class SuperintendenciaAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_filter = (['sre'])
    search_fields = ([])


admin.site.register(Superintendencia, SuperintendenciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Escola, EscolaAdmin)
admin.site.register(AgenciaTransporte, AgenciaTransporteAdmin)
admin.site.register(SRE, SreAdmin)
admin.site.register(Reclamante, ReclamanteAdmin)
admin.site.register(Reclamacao, ReclamacaoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)

admin.site.register(Comentario)






