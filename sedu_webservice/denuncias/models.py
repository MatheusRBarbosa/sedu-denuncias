from django.db import models
from django.contrib.auth.models import Group, User

class audit_entity(models.Model):
    
    #salvando automaticamente as datas de criação e atualização dos dados
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class abstract_entity(audit_entity):
    
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 
    
    class Meta:
        abstract = True
    

class SRE (abstract_entity):
    pass

class Superintendencia(Group):
    
    sre = models.ForeignKey(SRE,on_delete=models.CASCADE)
        
class Municipio(abstract_entity):
    superintendencia = models.ForeignKey(Superintendencia,on_delete=models.CASCADE)

class Escola(abstract_entity):
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

class Agencia_Transporte (abstract_entity):
    sre = models.ManyToManyField(SRE)
    superintendencia = models.ManyToManyField(Superintendencia)

class Aluno (abstract_entity):
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)

class Reclamante(abstract_entity):
    pass

class Reclamacao_Status (abstract_entity):
    pass

class Reclamacao (audit_entity):
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    protocolo = models.CharField(max_length=200)
    texto = models.TextField()
    agencia_transporte = models.ForeignKey(Agencia_Transporte, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE, blank=True, null=True)
    reclamante = models.ForeignKey(Reclamante, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.aluno.nome 

class Responsavel(audit_entity):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    superintendencia = models.ForeignKey(Superintendencia,on_delete=models.CASCADE)

class Comentario (audit_entity):
    texto = models.TextField()
    reclamacao = models.ForeignKey(Reclamacao,on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)
    


    
