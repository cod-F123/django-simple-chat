from django.urls import path
from . import views 

app_name = "chat"

urlpatterns = [
    path('echo/', views.EchoView.as_view(), name='echo'),
    path('', views.ChatListView.as_view(), name="chat-list"),
    path('detail/<str:chat_id>/', views.ChatDetailView.as_view(), name='chat-detail'),
    path('new-chat/', views.NewChatView.as_view(), name="new-chat"),
    path('new-chat/create-chat/', views.CreateNewChatView.as_view(), name="create-chat"),
    path('new-chat/add-contact/', views.CreateNewContactChatView.as_view(), name="add-contact"),
]
