from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Contact, Developer, DeveloperProject, Project,)
from .serializers import (ContactSerializer, DeveloperProjectSerializer,
                          DeveloperSerializer, ProjectSerializer)
from rest_framework import status

# 
class DeveloperRegistration(APIView):
    def post(self, request):
        developer_serializer = DeveloperSerializer(data=request.data)
        if developer_serializer.is_valid():
            developer = developer_serializer.save()

            # Handle projects data
            projects_data = request.data.get('projects', [])
            project_instances = []
            for project_data in projects_data:
                project_serializer = ProjectSerializer(data=project_data)
                if project_serializer.is_valid():
                    project_instance = project_serializer.save()
                    project_instances.append(project_instance)
                else:
                    return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Associate projects with the developer
            developer.projects.set(project_instances)

            return Response(developer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(developer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # 

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
    # permission_classes = [IsAuthenticated]

    def get(self, request, developer_id):
        developers = Developer.objects.get(id=developer_id)
        serializer = DeveloperSerializer(developers)
        return Response(serializer.data)
    
# class DeveloperCreate(APIView):
#     queryset = Developer.objects.all()
#     serializer_class = DeveloperSerializer

#     def post(self, request):
#         serializer = DeveloperSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

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
    # permission_classes = [IsAuthenticated]

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
    
class ContactList(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

class ContactDetail(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, contact_id):
        contacts = Contact.objects.get(id=contact_id)
        serializer = ContactSerializer(contacts)
        return Response(serializer.data)

class ContactCreate(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ContactUpdate(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def put(self, request, contact_id):
        contacts = Contact.objects.get(id=contact_id)
        serializer = ContactSerializer(contacts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class ContactDelete(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def delete(self, request, contact_id):
        contacts = Contact.objects.get(id=contact_id)
        contacts.delete()
        return Response(status=204)
    
class DeveloperProjectList(APIView):
    queryset = DeveloperProject.objects.all()
    serializer_class = DeveloperProjectSerializer

    def get(self, request):
        developer_projects = DeveloperProject.objects.all()
        serializer = DeveloperProjectSerializer(developer_projects, many=True)
        return Response(serializer.data)

class DeveloperProjectDetail(APIView):
    queryset = DeveloperProject.objects.all()
    serializer_class = DeveloperProjectSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, developer_project_id):
        developer_projects = DeveloperProject.objects.get(id=developer_project_id)
        serializer = DeveloperProjectSerializer(developer_projects)
        return Response(serializer.data)

class DeveloperProjectCreate(APIView):
    queryset = DeveloperProject.objects.all()
    serializer_class = DeveloperProjectSerializer

    def post(self, request):
        serializer = DeveloperProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DeveloperProjectUpdate(APIView):
    queryset = DeveloperProject.objects.all()
    serializer_class = DeveloperProjectSerializer

    def put(self, request, developer_project_id):
        developer_projects = DeveloperProject.objects.get(id=developer_project_id)
        serializer = DeveloperProjectSerializer(developer_projects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class DeveloperProjectDelete(APIView):
    queryset = DeveloperProject.objects.all()
    serializer_class = DeveloperProjectSerializer

    def delete(self, request, developer_project_id):
        developer_projects = DeveloperProject.objects.get(id=developer_project_id)
        developer_projects.delete()
        return Response(status=204)
    

