from django import forms
from .models import *

class WorkspaceForm(forms.ModelForm):
	class Meta:
		model = Workspace
		fields = ["name", "slug", "admin", "users"]
		labels = {
			"name" : "Название рабочей области",
			"slug" : "Поддомен",
			"admin" : "Администратор",
			"users" : "Пользователи"
		}