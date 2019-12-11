from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from denuncias.models import *
from django.contrib.auth.models import User
from datetime import date

@receiver(post_save, sender=Reclamacao)
def generate_protocol(sender, instance, created, **kwargs):
    if created:
        today = str(date.today()).replace("-", "")
        protocol_id = str(instance.id)
        
        while(len(protocol_id) < 6):
            protocol_id = "0" + protocol_id
        
        if(len(protocol_id) > 6):
            # Invertendo numero do id e pegando ate o sexto digito
            protocol_id = "".join(reversed(protocol_id))[:6]
            # Voltando para o numero correto apenas com os seis ultimos digitos do id
            protocol_id = "".join(reversed(protocol_id))

        final_protocol = today + str(instance.tipo_id) + protocol_id
        Reclamacao.objects.filter(pk=instance.id).update(protocolo=final_protocol)

@receiver(m2m_changed, sender=User.groups.through)
def create_responsavel(**kwargs):

    if(kwargs['action'] == 'post_add'):
        
        responsavel_data = {}
        sre_id = None
        for id in kwargs['pk_set']: 
            sre_id = id

        responsavel_data['sre'] = SRE.objects.get(id=sre_id)
        responsavel_data['usuario'] = kwargs['instance']

        try:
            responsavel = Responsavel.objects.get(usuario=responsavel_data['usuario'].id)
            responsavel.sre = responsavel_data['sre']
        except:
            responsavel = Responsavel(**responsavel_data)
        
        responsavel.save()


# @receiver(post_save, sender=Comentario)
# def update_status_reclamacao(sender, instance, created, **kwargs):
#     if created:
#         Reclamacao.objects.filter(pk=instance.reclamacao.id).update(status=2)

