from rest_framework.generics import ListAPIView

from .models import Project
from .serializers import ProjectsListSerializer


class ProjectsListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializer

