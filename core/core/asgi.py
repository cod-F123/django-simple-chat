"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
from channels.sessions import SessionMiddlewareStack
from django.core.asgi import get_asgi_application

from chat.websocket.routing import websocket_urlpatterns as chat_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http' : django_asgi_app,
    'websocket' : OriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat_routing
            )

        ),
        ["*"]
    )
})
