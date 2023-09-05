from django.urls import path

from dev_profile_app.api import RegisterApi

from .views import (ContactCreate, ContactDelete, ContactDetail, ContactList,
                    ContactUpdate, DeveloperDelete,
                    DeveloperDetail, DeveloperList, DeveloperProjectCreate,
                    DeveloperProjectDelete, DeveloperProjectDetail,
                    DeveloperProjectList, DeveloperProjectUpdate, DeveloperRegistration,
                    DeveloperUpdate, ProjectCreate, ProjectDelete,
                    ProjectDetail, ProjectList, ProjectUpdate)

app_name = 'dev_profile_app'

urlpatterns = [
    path('api/register/', RegisterApi.as_view()),

    path('api/developer_registration/', DeveloperRegistration.as_view(), name='developer_registration'),

    path('api/developers/', DeveloperList.as_view()),
    path('api/developers-detail/<int:developer_id>/', DeveloperDetail.as_view()),
    # path('api/developers/create/', DeveloperCreate.as_view()),
    path('api/developers/<int:developer_id>/update/', DeveloperUpdate.as_view()),
    path('api/developers/<int:developer_id>/delete/', DeveloperDelete.as_view()),

    path('api/projects/', ProjectList.as_view()),
    path('api/projects-detail/<int:project_id>/', ProjectDetail.as_view()),
    path('api/projects/create/', ProjectCreate.as_view()),
    path('api/projects/<int:project_id>/update/', ProjectUpdate.as_view()),
    path('api/patients/<int:project_id>/delete/', ProjectDelete.as_view()),

    path('api/contacts/', ContactList.as_view()),
    path('api/contacts-detail/<int:contact_id>/', ContactDetail.as_view()),
    path('api/contacts/create/', ContactCreate.as_view()),
    path('api/contacts/<int:contact_id>/update/', ContactUpdate.as_view()),
    path('api/contacts/<int:contact_id>/delete/', ContactDelete.as_view()),

    path('api/developer_projects/', DeveloperProjectList.as_view()),
    path('api/developer_projects-detail/<int:developer_project_id>/', DeveloperProjectDetail.as_view()),
    path('api/developer_projects/create/', DeveloperProjectCreate.as_view()),
    path('api/developer_projects/<int:developer_project_id>/update/', DeveloperProjectUpdate.as_view()),
    path('api/developer_projects/<int:developer_project_id>/delete/', DeveloperProjectDelete.as_view()),
]