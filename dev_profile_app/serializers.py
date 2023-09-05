from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Developer, Project, Contact, DeveloperProject

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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technologies_used', 'project_url', 'project_image', 'developer_project']


class DeveloperSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, required=False)
    class Meta:
        model = Developer
        fields = ['id', 'first_name', 'last_name', 'contact_email', 'profile_picture', 'bio', 'skills', 'github', 'linkedin', 'twitter', 'website', 'address', 'gender', 'projects'] 
    def create(self, validated_data):
        # Extract project data from validated_data
        projects_data = validated_data.pop('projects', [])
        
        # Create the developer instance
        developer = Developer.objects.create(**validated_data)

        # Create and associate projects
        for project_data in projects_data:
            Project.objects.create(developer=developer, **project_data)

        return developer



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message']


class DeveloperProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperProject
        fields = ['id', 'developer', 'project', 'role', 'start_date', 'end_date', 'is_currently_working']