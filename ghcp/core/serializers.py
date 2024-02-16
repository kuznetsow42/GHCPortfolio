from rest_framework import serializers

from .models import Bio, Skill, Language


class LanguageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class BasicsListSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()

    class Meta:
        model = Bio
        fields = "__all__"

    def get_skills(self, obj):
        return SkillListSerializer(Skill.objects.all(), many=True, context=self.context).data
    
    def get_languages(self, obj):
        return LanguageListSerializer(Language.objects.all(), many=True, context=self.context).data
        
