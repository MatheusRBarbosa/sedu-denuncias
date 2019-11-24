from django.db import models
from django.contrib.auth.models import Group, User
from django.urls import reverse


class AuditEntity(models.Model):
    
    # Salvando automaticamente as datas de criação e atualização dos dados
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
    

class SRE (Group):
    #nome = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Municipio(AbstractEntity):
    sre = models.ForeignKey(SRE, on_delete=models.CASCADE)
    cod_ibge = models.CharField(max_length=200)

class Escola(AbstractEntity):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    cod_inep = models.CharField(max_length=200)

class AgenciaTransporte (AbstractEntity):
    sre = models.ManyToManyField(SRE)
    
    class Meta:
        db_table = "denuncias_agencia_transporte"

class Aluno (AbstractEntity):
    ra = models.CharField(max_length=200, default="")
    cod_energia = models.CharField(max_length=200, default="")
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)

class Reclamante(AbstractEntity):
    email = models.EmailField(max_length=255, unique=True)

class ReclamacaoStatus (AbstractEntity):
    class Meta:
        db_table = "denuncias_reclamacao_status"

class Setor (AbstractEntity):
    pass

class TipoReclamacao (AbstractEntity):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    class Meta:
        db_table = "denuncias_tipo_reclamacao"

class Reclamacao (AuditEntity):
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.TextField()
    agencia_transporte = models.ForeignKey(AgenciaTransporte, on_delete=models.CASCADE, blank=True, null=True)
    reclamante = models.ForeignKey(Reclamante, on_delete=models.CASCADE, blank=True, null=True)
    cod_linha = models.CharField(max_length=60, default="", blank=True)
    protocolo = models.CharField(max_length=60, default="")
    tipo = models.ForeignKey(TipoReclamacao, on_delete=models.CASCADE, default=1)
    status = models.ForeignKey(ReclamacaoStatus, on_delete=models.CASCADE, default=1)
    data_ocorrido = models.DateTimeField()
    
    def __str__(self):
        return self.aluno.nome

    def get_absolute_url(self):
        return reverse('web_reclamacao_detail', kwargs={'pk':self.pk})

class Responsavel(AuditEntity):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    sre = models.ForeignKey(SRE,on_delete=models.CASCADE)
    
    def __str__(self):
        fullname = self.usuario.first_name + " " + self.usuario.last_name + " ({})".format(self.usuario.username)
        return fullname

class Comentario (AuditEntity):
    texto = models.TextField()
    reclamacao = models.ForeignKey(Reclamacao,on_delete=models.CASCADE, related_name='comentarios')
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)

    def __str__(self):
        fullname = self.responsavel.usuario.first_name + " " + self.responsavel.usuario.last_name
        user = self.responsavel.usuario.username
        replystring = "Resposta de {} ({})".format(fullname, user)
        return replystring