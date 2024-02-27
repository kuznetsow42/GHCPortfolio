from rest_framework import serializers
from .models import Chat, Message


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


    def validate(self, attrs):
        if not attrs.get("text") and not attrs.get("attachment"):
            raise serializers.ValidationError("Emtpy message")
        return super().validate(attrs)
        
