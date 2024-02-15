from django.db import models

PROFICIENCY_LEVELS = {
    "b": "Beginner",
    "i": "Intermediate",
    "a": "Advanced"
}


class SkillBase(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to="icons/")
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class SkillCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Skill Categories"


class Language(SkillBase):
    reading = models.CharField(max_length=1, choices=PROFICIENCY_LEVELS)
    speaking = models.CharField(max_length=1, choices=PROFICIENCY_LEVELS)


class Skill(SkillBase):
    level = models.CharField(choices=PROFICIENCY_LEVELS)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    

class Bio(models.Model):
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
