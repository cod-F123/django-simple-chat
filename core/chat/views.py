from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Member

# Create your views here.


class EchoView(TemplateView):
    template_name = 'chat/echo.html'

class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'chat/chat_list.html'
    context_object_name = "chats"

    def get_queryset(self):
        chats = self.model.objects.filter(members__user = self.request.user)

        return chats
    
class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Chat 
    template_name = 'chat/chat_detail.html'
    context_object_name = 'chat'
    pk_url_kwarg = 'chat_id'

    def get_object(self, chat_id):
        chat = get_object_or_404(Member, chat__chat_id = chat_id, user = self.request.user)

        return chat.chat
    
    def get(self, request, *args, **kwargs):
      
        self.object = self.get_object(kwargs.get("chat_id"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


