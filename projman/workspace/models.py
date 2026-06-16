from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy
from projman.registries.models import *

# Create your models here.
class Workspace(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="admin_workspaces")
	users = models.ManyToManyField(User, through="WorkspacePermissions", related_name="workspaces")

class WorkspacePermissions(models.Model):
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="workspace")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

	can_edit = models.BooleanField(default=False, null=False)

@receiver(pre_save, sender=Workspace)
def gen_slug(sender, instance, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)


class Project(models.Model):
	name = models.CharField(max_length=255)
	deadline = models.DateField()
	description = models.TextField(max_length=1024)
	customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_projects")
	tax_rate = models.IntegerField()
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="workspace_projects", null=False)

class ProjectResource(models.Model):
	class Types(models.IntegerChoices):
		EXECUTOR	= 0, gettext_lazy("Исполнитель")
		DEVICE		= 1, gettext_lazy("Оборудование")
		EMPLOYEE	= 2, gettext_lazy("Сотрудник")

	name = models.CharField(max_length=255)
	resource_type = models.IntegerField(choices=Types, default=Types.EXECUTOR)
	resource_id = models.IntegerField()
	service_name = models.CharField(max_length=255)
	deadline = models.DateField()
	marginality = models.IntegerField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="resources", null=False)