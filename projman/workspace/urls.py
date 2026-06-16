from django.urls import path
from . import views

urlpatterns = [
	path('', views.workspace),
	path('create', views.workspace_create),

	path('<slug:slug>', views.workspace_projects),
	path('<slug:slug>/edit', views.workspace_edit),
	path('<slug:slug>/delete', views.workspace_delete)
]
