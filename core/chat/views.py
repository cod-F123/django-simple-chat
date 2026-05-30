from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .models import Chat, Member
from .forms import ChatForm, CreateContactChatForm

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
    

class NewChatView(LoginRequiredMixin,TemplateView):
    template_name = "chat/new_chat.html"


class CreateNewChatView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]
    form_class = ChatForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        new_chat = form.save()

        return JsonResponse(data={"details" : {"status" : "chat_created", "chat_url": new_chat.get_absolute_url()}})
    
    def form_invalid(self, form):
        print(form.errors)
        return HttpResponseBadRequest(content=json.dumps({"details": {"status": "failed", "errors" : form.errors}}))
    

class CreateNewContactChatView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        form = CreateContactChatForm(initial={"owner": request.user}, data=request.POST)

        if form.is_valid():
            contact_chat = Chat.objects.create(owner = request.user, chat_type = "Private")
            Member.objects.create(chat = contact_chat, user = form.cleaned_data.get("contact"))

            return JsonResponse(data={"details" : {"status" : "chat_created", "chat_url": contact_chat.get_absolute_url()}})
        
        print(form.errors)

        return HttpResponseBadRequest(content=json.dumps({"details": {"status": "failed", "errors" : form.errors}}))


