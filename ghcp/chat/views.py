from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .models import Chat, Message
from .serializers import ChatCreateSerializer, MessageSerializer


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.set_cookie("chat", response.data["UUID"], httponly=True)
        return response


class MessageView(ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(chat=self.request.COOKIES.get("chat"))
    
    def create(self, request, *args, **kwargs):
        request.data["chat"] = request.COOKIES.get("chat")
        return super().create(request, *args, **kwargs)
