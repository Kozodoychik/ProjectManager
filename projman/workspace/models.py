from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy

# Create your models here.
class Workspace(models.Model):
	class Meta:
		permissions = [
			("can_manage_projects", "Может управлять проектами")
		]

	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="admin_workspaces")
	users = models.ManyToManyField(User, blank=True)

class WorkspacePermissions(models.Model):
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="permissions")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workspace_permissions")

	can_manage_projects = models.BooleanField(default=False, null=False)

@receiver(pre_save, sender=Workspace)
def gen_slug(sender, instance, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)