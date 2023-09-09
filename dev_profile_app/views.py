from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import AllData, Developer, Project, Stack, Technology
from .serializers import (AllDataSerializer, DeveloperSerializer,
                          ProjectSerializer, StackSerializer,
                          TechnologySerializer)

class AllDataListCreateView(generics.ListCreateAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer
    permission_classes = [IsAuthenticated]

class AllDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer
    permission_classes = [IsAuthenticated]

class DeveloperListCreateView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]

class DeveloperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]

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