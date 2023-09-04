from django.urls import path

from dev_profile_app.api import RegisterApi

from .views import DeveloperCreate, DeveloperDelete, DeveloperDetail, DeveloperList, DeveloperUpdate, ProjectCreate, ProjectDelete, ProjectDetail, ProjectList, ProjectUpdate

app_name = 'dev_profile_app'

urlpatterns = [
    path('api/register/', RegisterApi.as_view()),

    path('api/developers/', DeveloperList.as_view()),
    path('api/developers-detail/<int:developer_id>/', DeveloperDetail.as_view()),
    path('api/developers/create/', DeveloperCreate.as_view()),
    path('api/developers/<int:developer_id>/update/', DeveloperUpdate.as_view()),
    path('api/developers/<int:developer_id>/delete/', DeveloperDelete.as_view()),

    path('api/projects/', ProjectList.as_view()),
    path('api/projects-detail/<int:project_id>/', ProjectDetail.as_view()),
    path('api/projects/create/', ProjectCreate.as_view()),
    path('api/projects/<int:project_id>/update/', ProjectUpdate.as_view()),
    path('api/patients/<int:project_id>/delete/', ProjectDelete.as_view()),
]
