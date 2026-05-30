from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name="login-user"),
    path('register/', views.RegisterUserView.as_view(), name="register-user"),
    path('logout/', views.LogoutUserView.as_view(), name="logout-user"),
]
