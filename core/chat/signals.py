from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Chat, Member, Message

@receiver(post_save, sender = Chat)
def inital_chat(sender, instance , created, **kwargs):
    if created:
        
        Member.objects.create(chat= instance, user = instance.owner)

        if instance.chat_type != 'Private':
            Message.objects.create(chat= instance, sender = instance.owner, message_type = 'System', text = "chat created")