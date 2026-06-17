from django.db import models
from projman.registries.models import *
from projman.workspace.models import Workspace
from datetime import datetime, timedelta

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

	def get_type(self):
		return self.Types(self.resource_type).label
	
	def calculate_cost(self):
		match self.resource_type:
			case self.Types.EXECUTOR:
				return 1/3
			case self.Types.DEVICE:
				device = Hardware.objects.filter(id=self.resource_id)[0]
				units = (self.deadline - datetime.now().date()).days

				match device.unit:
					case device.Units.HOURS:
						units *= 24
					case device.Units.FULL:
						units = 1

				soz = device.unit_cost

				return soz * units

			case self.Types.EMPLOYEE:
				employee = Staff.objects.filter(id=self.resource_id)[0]
				cwd = (self.deadline - datetime.now().date()).days
				zp = employee.salary
				ns = employee.tax_rate / 100
				return (zp + (zp * ns))
		return 0