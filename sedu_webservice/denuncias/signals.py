from django.db.models.signals import post_save
from django.dispatch import receiver
from denuncias.models import Reclamacao
from datetime import date

@receiver(post_save, sender=Reclamacao)
def generateProtocol(sender, instance, created, **kwargs):
    if created:
        today = str(date.today()).replace("-", "")
        protocolId = str(instance.id)
        
        while(len(protocolId) < 6):
            protocolId = "0" + protocolId

        finalProtocol = today + protocolId
        Reclamacao.objects.filter(pk=instance.id).update(protocolo=finalProtocol)