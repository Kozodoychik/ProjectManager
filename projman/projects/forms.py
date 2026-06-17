from django import forms
from projman.core.widgets import DateInput
from .models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ["name", "deadline", "description", "customer", "tax_rate"]
		labels = {
			"name" : "Название",
			"deadline" : "Дата окончания",
			"description" : "Описание",
			"customer" : "Заказчик",
			"tax_rate" : "Налоговая ставка"
		}
		widgets = {
			"deadline" : DateInput(format="%Y-%m-%d")
		}

class ProjectResourceForm(forms.ModelForm):
	class Meta:
		model = ProjectResource
		fields = ["name", "deadline", "service_name", "marginality"]
		labels = {
			"name" : "Название ресурса",
			"deadline" : "Дата окончания",
			"service_name" : "Название услуги",
			"marginality" : "Маржинальность"
		}
		widgets = {
			"deadline" : DateInput(format="%Y-%m-%d")
		}

class ResourceTypeForm(forms.ModelForm):
	class Meta:
		model = ProjectResource
		fields = ["resource_type"]
		labels = {
			"resource_type" : "Выберите тип ресурса"
		}