from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(default="", null=False)
	admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="admin_workspaces")
	users = models.ManyToManyField(User, through="WorkspacePermissions", related_name="workspaces")

class WorkspacePermissions(models.Model):
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="workspace")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

	can_edit = models.BooleanField(default=False, null=False)