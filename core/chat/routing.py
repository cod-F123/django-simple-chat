from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/echo/', consumers.EchoComsumer.as_asgi()),
    path('ws/chat/<str:chat_id>/', consumers.ChatConsomer.as_asgi()),
]