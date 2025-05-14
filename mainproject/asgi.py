"""
ASGI config for mainproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainproject.settings')
django.setup()
application = get_default_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from mainapp.routing import websocket_urlpatterns
import mainapp

application = ProtocolTypeRouter({
     "http": get_default_application(),
     "websocket": AuthMiddlewareStack(
          URLRouter(
               mainapp.routing.websocket_urlpatterns
          )
     ),
})
