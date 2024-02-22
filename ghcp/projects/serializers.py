from rest_framework import serializers

from .models import Project


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth = 1
