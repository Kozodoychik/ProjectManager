from django import forms
from projman.core.models import Company

class ParamForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ["name", "head_name", "head_pos", "contact_number", "contact_email"]
		labels = {
			"name" : "Наименование организации",
			"head_name" : "ФИО руководителя",
			"head_pos" : "Должность руководителя",
			"contact_number" : "Контактный телефон",
			"contact_email" : "Контактный Email"
		}