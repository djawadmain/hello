"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import CookieMiddleware, SessionMiddlewareStack
from django.core.asgi import get_asgi_application

from main import routing as main_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        CookieMiddleware(
            SessionMiddlewareStack(
                URLRouter(
                    main_routing.websocket_urlpatterns
                )
            )
        )
    ),
    'http': get_asgi_application()
})
