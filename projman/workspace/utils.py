from django.http import HttpRequest
from .models import *

def can_manage_projects(request: HttpRequest, slug):
	workspace = Workspace.objects.get(slug=slug)
	if not workspace: return False
	if workspace.admin == request.user or request.user.is_superuser: return True

	permissions = WorkspacePermissions.objects.filter(user=request.user, workspace=workspace)
	if not permissions: return False

	return permissions[0].can_manage_projects