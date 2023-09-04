from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Developer, Project
from .serializers import DeveloperSerializer, ProjectSerializer


class DeveloperList(APIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)

class DeveloperDetail(APIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, developer_id):
        developers = Developer.objects.get(id=developer_id)
        serializer = DeveloperSerializer(developers)
        return Response(serializer.data)

class DeveloperCreate(APIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def post(self, request):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DeveloperUpdate(APIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def put(self, request, developer_id):
        developers = Developer.objects.get(id=developer_id)
        serializer = DeveloperSerializer(developers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
class DeveloperDelete(APIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def delete(self, request, developer_id):
        developers = Developer.objects.get(id=developer_id)
        developers.delete()
        return Response(status=204)



class ProjectList(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        projects = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)

class ProjectCreate(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProjectUpdate(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def put(self, request, project_id):
        projects = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(projects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class ProjectDelete(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def delete(self, request, project_id):
        projects = Project.objects.get(id=project_id)
        projects.delete()
        return Response(status=204)