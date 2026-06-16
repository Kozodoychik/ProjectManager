from django.urls import path, include
from . import views

patterns_project = [
	path('edit/', views.project_edit),
	path('delete/', views.project_delete),
	path('resources/', views.project_edit),
]

urlpatterns = [
	path('bulk-delete/', views.projects_bulk_delete),

	path('<int:project_id>/', include((patterns_project, 'project'), namespace='project')),
]
