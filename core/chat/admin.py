from django.contrib import admin
from .models import Chat, Member, Message

# Register your models here.

class MemberInlineAdmin(admin.StackedInline):
    model = Member
    extra = 1

class MessageInlineAdmin(admin.StackedInline):
    model = Message
    extra = 1

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['title', 'chat_type', 'created_date']

    inlines = [MemberInlineAdmin, MessageInlineAdmin]
