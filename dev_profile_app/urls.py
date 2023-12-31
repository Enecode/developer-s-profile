# webapp/urls.py
from django.urls import path

from dev_profile_app.api import RegisterApi

from .views import (AllDataDetailView, AllDataListCreateView,
                    DeveloperDetailView, DeveloperListCreateView, ExperienceDetailView, ExperienceListCreateView,
                    ProjectDetailView,
                    ProjectListCreateView, StackDetailView,
                    StackListCreateView, TechnologyDetailView, EducationDetailView, EducationListCreateView,
                    TechnologyListCreateView)

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/developers/', DeveloperListCreateView.as_view(), name='developer-list-create'),
    path('api/developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),

    path('api/educations/', EducationListCreateView.as_view(), name='education-list-create'),
    path('api/educations/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),

   
    path('api/experiences/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('api/experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),

    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('api/stacks/', StackListCreateView.as_view(), name='stack-list-create'),
    path('api/stacks/<int:pk>/', StackDetailView.as_view(), name='stack-detail'),

    path('api/technologies/', TechnologyListCreateView.as_view(), name='technology-list-create'),
    path('api/technologies/<int:pk>/', TechnologyDetailView.as_view(), name='technology-detail'),
    
    path('api/all_data/', AllDataListCreateView.as_view(), name='all_data-list-create'),
    path('api/all_data/<int:pk>/', AllDataDetailView.as_view(), name='all_data-detail'),
]
