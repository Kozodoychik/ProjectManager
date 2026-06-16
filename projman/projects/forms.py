from django import forms
from projman.core.widgets import DateInput
from .models import Project

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