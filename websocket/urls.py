from django.urls import path
from .views import *

app_name='websocket'
urlpatterns=[
    path('test/', test, name ='test'),
    path('connect/', connect, name ='connect'),
    path('disconnect/', disconnect, name ='disconnect'),
    path('send_message/', send_message, name ='send_message'),
]
