from django import forms
from .models import *
from projman.core.widgets import DateInput
from projman.projects.models import *

class WorkspaceForm(forms.ModelForm):
	class Meta:
		model = Workspace
		fields = ["name", "slug"]
		labels = {
			"name" : "Название рабочей области",
			"slug" : "Поддомен",
		}

	def __init__(self, *args, **kwargs):
		super(WorkspaceForm, self).__init__(*args, **kwargs)

		self.fields["slug"].required = False