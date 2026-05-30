from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login , get_user_model
from .forms import RegisterUserForm

# Create your views here.

class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    
    def get_success_url(self):
        return "/"

class RegisterUserView(CreateView):
    template_name = "accounts/register.html"
    success_url = "/"
    form_class = RegisterUserForm
    

    def form_valid(self, form):

        self.object = form.save()

        login(self.request, user=self.object)

        return redirect("chat:chat-list")


class LogoutUserView(LogoutView):

    def get_success_url(self):
        return "/accounts/login/"
        

