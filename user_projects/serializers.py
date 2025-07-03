from rest_framework import serializers
from .models import UserProject

class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = '__all__'

    def validate(self, data):
        # Example validation: Ensure name is not empty
        if not data.get('name'):
            raise serializers.ValidationError({"name": "This field is required."})

        # Example validation: Ensure deployment_url is a valid URL if provided
        if data.get('deployment_url') and not data['deployment_url'].startswith('http'):
            raise serializers.ValidationError({"deployment_url": "Enter a valid URL."})

        return data
