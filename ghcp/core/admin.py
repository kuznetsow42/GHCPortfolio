from django.contrib import admin

from .models import Language, HardSkill, SoftSkill, Link, Bio, SoftSkillStory


admin.site.register(SoftSkill)
admin.site.register(SoftSkillStory)
admin.site.register(HardSkill)
admin.site.register(Language)
admin.site.register(Link)
admin.site.register(Bio)
