from django.contrib import admin

from .models import Language, HardSkill, SoftSkill, Bio, SoftSkillStory


admin.site.register(SoftSkill)
admin.site.register(SoftSkillStory)
admin.site.register(HardSkill)
admin.site.register(Language)
admin.site.register(Bio)
