from django.db import models
from django.contrib.auth.models import User
import uuid


def get_file_path(instance, filename) -> str:
    return f"messages/{instance.chat}/{filename}"


class Chat(models.Model):
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="chat", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.UUID)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    is_reply = models.BooleanField(default=False)
    is_readed = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to=get_file_path, blank=True)

    def __str__(self) -> str:
        return self.message or "ATTACHMENT"
