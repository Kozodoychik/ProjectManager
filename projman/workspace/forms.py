from django import forms
from .models import *
from projman.core.widgets import DateInput

class WorkspaceForm(forms.ModelForm):
	class Meta:
		model = Workspace
		fields = ["name", "slug", "admin"]
		labels = {
			"name" : "Название рабочей области",
			"slug" : "Поддомен",
			"admin" : "Администратор",
		}

	def __init__(self, *args, **kwargs):
		super(WorkspaceForm, self).__init__(*args, **kwargs)

		self.fields["slug"].required = False

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
			"deadline" : DateInput()
		}