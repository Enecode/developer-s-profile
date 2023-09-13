from django.contrib.auth.models import User
from rest_framework import serializers

from .models import AllData, Developer, Project, Stack, Technology, Experience, Education


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

class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllData
        fields = '__all__'

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_url']

class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ['id', 'first_name', 'last_name', 'picture', 'email', 'bio', 'skills', 'github', 'linkedin', 'twitter', 'website', 'address', 'gender', 'stacks', 'projects', 'experiences', 'educations', 'technologies', ]

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'title', 'description', 'start_date', 'end_date')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'school', 'degree', 'start_date', 'end_date')