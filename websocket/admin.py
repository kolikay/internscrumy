from django.contrib import admin
from websocket.models import ChatMessage, CreateConnection


admin.site.register(CreateConnection)
admin.site.register(ChatMessage)

