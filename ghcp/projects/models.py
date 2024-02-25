from django.db import models

from core.models import HardSkill


class Project(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="projects")
    pet = models.BooleanField(default=True)
    description = models.TextField()
    link = models.CharField(max_length=300)
    tools = models.ManyToManyField(HardSkill, related_name="projects")
    demo = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
