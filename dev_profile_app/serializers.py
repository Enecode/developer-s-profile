from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Developer, Project


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'password', 'email')
        extra_kwargs = \
            {
                'password': {'write_only': True},
            }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'bio', 'skills', 'github', 'linkedin', 'twitter', 'website', 'address', 'gender']
        extra_kwargs = {'user': {'read_only': True}}

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ['id', 'title', 'description', 'technologies_used', 'project_url', 'developer']
#         extra_kwargs = {'developer': {'read_only': True}}

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technologies_used', 'project_url', 'developer']