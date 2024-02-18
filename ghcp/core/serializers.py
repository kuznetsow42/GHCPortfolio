from rest_framework import serializers

from .models import Bio, SoftSkill, Language, HardSkill


class LanguageListSerializer(serializers.ModelSerializer):
    speaking = serializers.CharField(source="get_speaking_display")
    reading = serializers.CharField(source="get_reading_display")

    class Meta:
        model = Language
        fields = "__all__"


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = "__all__"
        depth = 1


class HardSkillSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")

    class Meta:
        model = HardSkill
        fields = "__all__"


class BasicsListSerializer(serializers.ModelSerializer):
    soft_skills = serializers.SerializerMethodField()
    hard_skills = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()

    class Meta:
        model = Bio
        fields = "__all__"

    def get_soft_skills(self, obj):
        return SoftSkillSerializer(SoftSkill.objects.all(), many=True, context=self.context).data
    
    def get_hard_skills(self, obj):
        return HardSkillSerializer(HardSkill.objects.all(), many=True, context=self.context).data
    
    def get_languages(self, obj):
        return LanguageListSerializer(Language.objects.all(), many=True, context=self.context).data
        
