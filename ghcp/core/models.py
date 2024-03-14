from datetime import date
from django.utils import timezone
from django.db import models
from django.db.models import F
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay

PROFICIENCY_LEVELS = {
    "b": "Beginner",
    "i": "Intermediate",
    "a": "Advanced"
}

class SkillBase(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class Language(SkillBase):
    reading = models.CharField(max_length=1, choices=PROFICIENCY_LEVELS)
    speaking = models.CharField(max_length=1, choices=PROFICIENCY_LEVELS)
    icon = models.ImageField(upload_to="icons/")


class HardSkill(SkillBase):
    icon = models.ImageField(upload_to="icons/")
    level = models.CharField(choices=PROFICIENCY_LEVELS)


class SoftSkillStory(models.Model):
    image = models.ImageField(upload_to="team/")
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name_plural = "Soft skills stories"


class SoftSkill(SkillBase):
    stories = models.ManyToManyField(SoftSkillStory, "soft_skills", blank=True)
    

class Link(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons/")

    def __str__(self) -> str:
        return self.name


class Bio(models.Model):
    resume = models.FileField(upload_to="files/")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photos/")
    birth_date = models.DateField()
    location = models.CharField(max_length=70)
    greating_message = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Bio"
