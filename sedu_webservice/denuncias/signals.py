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

# @receiver(post_save, sender=Comentario)
# def update_status_reclamacao(sender, instance, created, **kwargs):
#     if created:
#         Reclamacao.objects.filter(pk=instance.reclamacao.id).update(status=2)

@receiver(m2m_changed, sender=User.groups.through)
def create_responsavel(**kwargs):
    # Se o responsavel ja existir, apenas atualizar a sre dele.
        # POST_ADD
        # POST_REMOVE
    # Mas se ele for da SEDU ? Qual vai ser a SRE
    # Posso assumir que quando um usuario tem mais de uma SRE eh NECESSARIAMENTE A SEDU ?!

    # Apenas a ultima SRE eh salva
    # No caso, se for SEDU, todas as outras SRE vao precisar serem adicionadas primeiro e por ultimo a SEDU.

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
        print(responsavel.sre)
    
    # Se for um remove eu preciso tratar ? Uma reclamacao ( que nao pode ser apagada ), pode ficar sem responsavel pelos comentarios ?
    #elif(kwargs['action'] == 'post_remove'):
    #    user = kwargs['instance']
    #    resp = Responsavel.objects.get(usuario=user.id) 
    #    print(resp.sre)
    #   print('=============APAGANDO===========')

