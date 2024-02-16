from rest_framework.generics import RetrieveAPIView

from .models import Bio
from .serializers import BasicsListSerializer


class BasicsListView(RetrieveAPIView):
    serializer_class = BasicsListSerializer

    def get_object(self):
        return Bio.objects.first()
