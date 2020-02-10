from django.contrib import admin
from websocket.models import ChatMessage, Connection

admin.site.register(Connection )
admin.site.register(ChatMessage)
