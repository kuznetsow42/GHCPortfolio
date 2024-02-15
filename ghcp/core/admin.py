from django.contrib import admin

from .models import SkillCategory, Language, Skill, Bio


admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(SkillCategory)
admin.site.register(Bio)
