from django.db import models
from django.contrib.auth.models import Group, User


class AuditEntity(models.Model):
    
    #salvando automaticamente as datas de criação e atualização dos dados
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractEntity(AuditEntity):
    
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 
    
    class Meta:
        abstract = True
    

class SRE (AbstractEntity):
    pass

class Superintendencia(Group):
    
    sre = models.ForeignKey(SRE,on_delete=models.CASCADE)
        
class Municipio(AbstractEntity):
    superintendencia = models.ForeignKey(Superintendencia,on_delete=models.CASCADE)

class Escola(AbstractEntity):
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

class AgenciaTransporte (AbstractEntity):
    sre = models.ManyToManyField(SRE)
    superintendencia = models.ManyToManyField(Superintendencia)
    
    class Meta:
        db_table = "denuncias_agencia_transporte"

class Aluno (AbstractEntity):
    ra = models.CharField(max_length=200, default="")
    cod_energia = models.CharField(max_length=200, default="")
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)

class Reclamante(AbstractEntity):
    pass

class ReclamacaoStatus (AbstractEntity):
    pass

    class Meta:
        db_table = "denuncias_reclamacao_status"

class TipoReclamacao (AbstractEntity):
    pass
    class Meta:
        db_table = "denuncias_tipo_reclamacao"

class Reclamacao (AuditEntity):
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.TextField()
    agencia_transporte = models.ForeignKey(AgenciaTransporte, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE, blank=True, null=True)
    reclamante = models.ForeignKey(Reclamante, on_delete=models.CASCADE, blank=True, null=True)
    cod_linha = models.CharField(max_length=60, default="")
    protocolo = models.CharField(max_length=60, default="")
    tipo = models.ForeignKey(TipoReclamacao, on_delete=models.CASCADE, default=1)
    status = models.ForeignKey(ReclamacaoStatus, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.aluno.nome 

class Responsavel(AuditEntity):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    superintendencia = models.ForeignKey(Superintendencia,on_delete=models.CASCADE)
    
    def __str__(self):
        fullName = self.usuario.first_name + " " + self.usuario.last_name + " ({})".format(self.usuario.username)
        return fullName

class Comentario (AuditEntity):
    texto = models.TextField()
    reclamacao = models.ForeignKey(Reclamacao,on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)

    def __str__(self):
        fullName = self.responsavel.usuario.first_name + " " + self.responsavel.usuario.last_name
        user = self.responsavel.usuario.username
        replyString = "Resposta de {} ({})".format(fullName, user)
        return replyString