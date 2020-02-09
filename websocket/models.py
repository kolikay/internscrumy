from django.db import models

# Create your models here.


class CreateConnection(models.Model):
    connection_id = models.CharField(max_length=255)

class ChatMessage(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=20, null=True)