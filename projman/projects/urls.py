from django.urls import path, include
from . import views

patterns_resources = [
	path('', views.project_resources),
	path('add/', views.project_resource_add),
	path('bulk-delete/', views.project_resources_bulk_remove),
	path('<int:resource_id>/delete/', views.project_resource_remove),
]

patterns_project = [
	path('edit/', views.project_edit),
	path('delete/', views.project_delete),
	path('resources/', include((patterns_resources, 'resources'), namespace='resources')),
]

urlpatterns = [
	path('<int:project_id>/', include((patterns_project, 'project'), namespace='project')),
]
