from django.db import models
from django.utils.timezone import now
from projman.registries.models import *
from projman.workspace.models import Workspace

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=255)
	start_date = models.DateField(default=now)
	deadline = models.DateField()
	description = models.TextField(max_length=1024)
	customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_projects")
	tax_rate = models.IntegerField()
	workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="workspace_projects", null=False)

	def calculate_cost(self):
		sum = 0
		for resource in self.resources.all():
			sum += resource.calculate_cost()
		return sum
	
	def calculate_cost_with_marginality(self):
		sum = 0
		for resource in self.resources.all():
			sum += resource.calculate_total()
		return sum
	
	def calculate_total(self):
		sp = self.calculate_cost_with_marginality()
		return sp + (sp * (self.tax_rate / 100))
	
	def calculate_profit(self):
		sum = 0
		for resource in self.resources.all():
			sum += resource.calculate_total() - resource.calculate_cost()
		return sum

class ProjectResource(models.Model):
	class Types(models.IntegerChoices):
		EXECUTOR	= 0, gettext_lazy("Исполнитель")
		DEVICE		= 1, gettext_lazy("Оборудование")
		EMPLOYEE	= 2, gettext_lazy("Сотрудник")

	name = models.CharField(max_length=255)
	resource_type = models.IntegerField(choices=Types, default=Types.EXECUTOR)
	resource_id = models.IntegerField()
	service_name = models.CharField(max_length=255)
	start_date = models.DateField(default=now)
	deadline = models.DateField()
	marginality = models.IntegerField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="resources", null=False)

	def get_type(self):
		return self.Types(self.resource_type).label
	
	def calculate_cost(self):
		match self.resource_type:
			case self.Types.EXECUTOR:
				executor = Executors.objects.get(id=self.resource_id)
				units = (self.deadline - self.start_date).days

				match executor.unit:
					case executor.Units.HOURS:
						units *= 24
					case executor.Units.FULL:
						units = 1

				suz = executor.unit_cost
				ns = executor.tax_rate / 100

				return ((units * suz) + ((units * suz) * ns))

			case self.Types.DEVICE:
				device = Hardware.objects.get(id=self.resource_id)
				units = (self.deadline - self.start_date).days

				match device.unit:
					case device.Units.HOURS:
						units *= 24
					case device.Units.FULL:
						units = 1

				soz = device.unit_cost

				return soz * units

			case self.Types.EMPLOYEE:
				employee = Staff.objects.get(id=self.resource_id)
				cwd = (self.deadline - self.start_date).days
				zp = employee.salary
				ns = employee.tax_rate / 100
				return (zp + (zp * ns))
		return 0
	
	def calculate_total(self):
		return self.calculate_cost() / (1 - (self.marginality / 100))