from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Superintendencia)
admin.site.register(Municipio)
admin.site.register(Escola)
admin.site.register(Agencia_Transporte)
admin.site.register(SRE)
admin.site.register(Aluno)
admin.site.register(Reclamante)

class ReclamacaoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('aluno','protocolo','agencia_transporte','municipio', 'reclamante')
    list_filter = ('aluno','protocolo','agencia_transporte','municipio', 'reclamante')
    search_fields = (['protocolo'])

admin.site.register(Reclamacao, ReclamacaoAdmin)

admin.site.register(Responsavel)
admin.site.register(Comentario)






