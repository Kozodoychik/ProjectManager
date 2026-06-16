from django.db import models
from projman.registries.models import *
from projman.workspace.models import Workspace

# Create your models here.
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