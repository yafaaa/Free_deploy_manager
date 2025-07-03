from rest_framework import serializers
from .models import Platform, ProgrammingLanguage, DatabaseType, Feature

class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'

class DatabaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseType
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    supported_languages = ProgrammingLanguageSerializer(many=True, read_only=True)
    supported_databases = DatabaseTypeSerializer(many=True, read_only=True)
    supported_features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Platform
        fields = '__all__'
