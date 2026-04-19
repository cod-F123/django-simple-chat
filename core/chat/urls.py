from django.urls import path
from . import views 

app_name = "chat"

urlpatterns = [
    path('echo/', views.EchoView.as_view(), name='echo'),
    path('', views.ChatListView.as_view(), name="chat-list"),
    path('detail/<str:chat_id>/', views.ChatDetailView.as_view(), name='chat-detail')
]
