from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AllData, Developer, Experience, Project, Stack, Education, Technology
from .serializers import (AllDataSerializer, DeveloperSerializer,
                          ExperienceSerializer, ProjectSerializer, EducationSerializer,
                          StackSerializer, TechnologySerializer)


class AllDataListCreateView(generics.ListCreateAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer


class AllDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer


class DeveloperListCreateView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class StackListCreateView(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class StackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class TechnologyListCreateView(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class ExperienceListCreateView((generics.ListCreateAPIView)):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationListCreateView((generics.ListCreateAPIView)):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer