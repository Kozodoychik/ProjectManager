from django import forms
from projman.core.widgets import DateInput
from .models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ["name", "start_date", "deadline", "description", "customer", "tax_rate"]
		labels = {
			"name" : "Название",
			"start_date" : "Дата начала выполнения",
			"deadline" : "Дата окончания выполнения",
			"description" : "Описание",
			"customer" : "Заказчик",
			"tax_rate" : "Налоговая ставка (проценты)"
		}
		widgets = {
			"start_date" : DateInput(format="%Y-%m-%d"),
			"deadline" : DateInput(format="%Y-%m-%d")
		}

class ProjectResourceForm(forms.ModelForm):
	class Meta:
		model = ProjectResource
		fields = ["name", "start_date", "deadline", "service_name", "marginality"]
		labels = {
			"name" : "Название ресурса",
			"start_date" : "Дата начала выполнения",
			"deadline" : "Дата окончания выполнения",
			"service_name" : "Название услуги",
			"marginality" : "Маржинальность (проценты)"
		}
		widgets = {
			"start_date" : DateInput(format="%Y-%m-%d"),
			"deadline" : DateInput(format="%Y-%m-%d")
		}

class ResourceTypeForm(forms.ModelForm):
	class Meta:
		model = ProjectResource
		fields = ["resource_type"]
		labels = {
			"resource_type" : "Выберите тип ресурса"
		}