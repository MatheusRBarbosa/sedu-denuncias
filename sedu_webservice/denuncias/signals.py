from django.db.models.signals import post_save
from django.dispatch import receiver
from denuncias.models import Reclamacao, Comentario
from datetime import date

@receiver(post_save, sender=Reclamacao)
def generateProtocol(sender, instance, created, **kwargs):
    if created:
        today = str(date.today()).replace("-", "")
        protocolId = str(instance.id)
        
        while(len(protocolId) < 6):
            protocolId = "0" + protocolId
        
        if(len(protocolId) > 6):
            # Invertendo numero do id e pegando ate o sexto digito
            protocolId = "".join(reversed(protocolId))[:6]
            # Voltando para o numero correto apenas com os seis ultimos digitos do id
            protocolId = "".join(reversed(protocolId))

        finalProtocol = today + str(instance.tipo_id) + protocolId
        Reclamacao.objects.filter(pk=instance.id).update(protocolo=finalProtocol)

@receiver(post_save, sender=Comentario)
def updateStatusReclamacao(sender, instance, created, **kwargs):
    if created:
        Reclamacao.objects.filter(pk=instance.reclamacao.id).update(status=2)