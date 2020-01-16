from django.db import models
from django.contrib.auth.models import Group, User
from django.urls import reverse
import uuid

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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SREs"

class Municipio(AbstractEntity):
    sre = models.ForeignKey(SRE, on_delete=models.CASCADE)
    cod_ibge = models.CharField(max_length=200)

class Escola(AbstractEntity):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    cod_inep = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, blank=True, null=True, default="")

class AgenciaTransporte (AbstractEntity):
    sre = models.ManyToManyField(SRE)
    
    class Meta:
        db_table = "denuncias_agencia_transporte"
        verbose_name = "Agência de transporte"
        verbose_name_plural = "Agências de transporte"
        
        

class Aluno (AbstractEntity):
    ra = models.CharField(max_length=200, blank=True, default="")
    cod_energia = models.CharField(max_length=200, blank=True, null=True, default="")
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

class Reclamante(AbstractEntity):
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True, default="")
    sub_novo = models.UUIDField(editable=False, blank=True, null=True)

class ReclamacaoStatus (AbstractEntity):
    class Meta:
        db_table = "denuncias_reclamacao_status"

class Setor (AbstractEntity):
    pass

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Setores"

class TipoReclamacao (AbstractEntity):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "denuncias_tipo_reclamacao"
        verbose_name_plural = "Tipos de reclamações"

class Turno(AbstractEntity):
    pass

    def __str__(self):
        return self.nome

class Rota(AbstractEntity):
    cod_linha = models.CharField(max_length=60, default="", blank=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name='turno')
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola')

    def __str__(self):
        return self.cod_linha +" | " + self.turno.nome + " | " + self.nome 

class Papel(AbstractEntity):
    pass

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Papeis"
    

class Reclamacao (AuditEntity):
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.TextField()
    papel = models.ForeignKey(Papel, on_delete=models.CASCADE)
    outro_papel = models.CharField(max_length=255, blank=True, default="")
    agencia_transporte = models.ForeignKey(AgenciaTransporte, on_delete=models.CASCADE, null=True)
    reclamante = models.ForeignKey(Reclamante, on_delete=models.CASCADE, null=True)
    protocolo = models.CharField(max_length=60, default="")
    status = models.ForeignKey(ReclamacaoStatus, on_delete=models.CASCADE, default=1)
    data_ocorrido = models.DateTimeField()

    # Atributos de reclamacao de transporte
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    placa_veiculo = models.CharField(max_length=255, blank=True, default="")
    tipo = models.ForeignKey(TipoReclamacao, on_delete=models.CASCADE, default=1)
    outro_tipo = models.CharField(max_length=255, blank=True, default="")

    # Sre responsavel pela reclamacao
    sre_responsavel = models.ForeignKey(SRE, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.aluno.nome

    class Meta:
        verbose_name_plural = "Reclamações"

class Responsavel(AuditEntity):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    sre = models.ForeignKey(SRE,on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        fullname = self.usuario.first_name + " " + self.usuario.last_name + " ({})".format(self.usuario.username)
        return fullname
    
    class Meta:
        verbose_name_plural = "Responsáveis"

class Comentario (AuditEntity):
    texto = models.TextField()
    reclamacao = models.ForeignKey(Reclamacao,on_delete=models.CASCADE, related_name='comentarios')
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)

    def __str__(self):
        fullname = self.responsavel.usuario.first_name + " " + self.responsavel.usuario.last_name
        user = self.responsavel.usuario.username
        replystring = "Resposta de {} ({})".format(fullname, user)
        return replystring

class ParecerFinal (AuditEntity):
    texto = models.TextField()
    reclamacao = models.ForeignKey(Reclamacao,on_delete=models.CASCADE, related_name='parecer_final')
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)

    def __str__(self):
        fullname = self.responsavel.usuario.first_name + " " + self.responsavel.usuario.last_name
        user = self.responsavel.usuario.username
        replystring = "Parecer de {} ({})".format(fullname, user)
        return replystring
    
    class Meta:
        db_table = "denuncias_parecer_final"

class Token(AbstractEntity):
    key = models.UUIDField(editable=False, default=uuid.uuid4)

