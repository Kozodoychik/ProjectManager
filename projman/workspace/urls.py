from django.urls import path, include
from . import views


patterns_workspace = [
	path('', views.workspace_projects),
	path('create/', views.workspace_project_create),
	path('edit/', views.workspace_edit),
	path('delete/', views.workspace_delete),
	path('users/', views.workspace_users)
]

urlpatterns = [
	path('', views.workspace),
	path('create/', views.workspace_create),

	path('<slug:slug>/', include((patterns_workspace, 'workspace'), namespace='workspace')),

	path('<slug:workspace_slug>/', include('projman.projects.urls'))
]
