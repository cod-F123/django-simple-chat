from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

User = get_user_model()

# Create your models here.

class Chat(models.Model):
    
    CHAT_TYPES = (
        ('Private', 'Private'),
        ('Channel', 'Channel'),
        ('Group', 'Group')
    )

    title = models.CharField(max_length=200 , blank=True, null=True)

    chat_id = models.CharField(max_length=255, blank=True, null=True, unique=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_chats")

    description = models.TextField(blank=True, null=True)

    chat_type = models.CharField(max_length=7, choices=CHAT_TYPES, default='Private')

    created_date = models.DateTimeField(auto_now_add=True)    

    @property
    def members_count(self):
        return self.members.count()
    
    def save(self, *args, **kwargs):

        if self.chat_id is None:
            self.chat_id = str(uuid.uuid4()).replace("-","")[:20] + str(timezone.now().microsecond)
        
        super().save(*args, **kwargs)

class Member(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="members")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")

    joined_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):

    MESSAGE_TYPES  = (
        ('Message','Message'),
        ('System', 'System')
    )

    FILE_TYPES = (
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Audio', 'Audio'),
        ('File', 'File')
    )

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sended_messages")

    text = models.TextField(blank=True, null=True)

    file = models.FileField(blank=True, null=True)

    message_type = models.CharField(max_length=7 , choices=MESSAGE_TYPES, default='Message')
    file_type = models.CharField(max_length=5, choices=FILE_TYPES, default='File')

    is_edited = models.BooleanField(default= False)

    sended_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    @property
    def seen_count(self):
        return 1






