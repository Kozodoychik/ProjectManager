from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customers
		fields = ["inn", "customer_type", "name", "customer_name", "contact_email", "contact_number"]
		labels = {
			"inn" : "ИНН",
			"customer_type" : "Тип заказчика",
			"name" : "Название",
			"customer_name" : "ФИО руководителя",
			"contact_email" : "Контактный адрес эл. почты",
			"contact_number" : "Контактный телефон"
		}

class ExecutorForm(forms.ModelForm):
	class Meta:
		model = Executors
		fields = ["name", "registration_type", "tax_rate", "unit", "unit_cost"]
		labels = {
			"name" : "ФИО исполнителя",
			"registration_type" : "Тип оформления",
			"tax_rate" : "Расчётная налоговая ставка",
			"unit" : "Единица измерения",
			"unit_cost" : "Стоимость услуг за единицу измерения"
		}

class DeviceForm(forms.ModelForm):
	class Meta:
		model = Hardware
		fields = ["name", "description", "purchase_type", "operating_cost", "unit", "unit_cost"]
		labels = {
			"name" : "Наименование",
			"description" : "Описание",
			"purchase_type" : "Тип приобретения",
			"operating_cost" : "Эксплуатационная стоимость",
			"unit" : "Единица измерения",
			"unit_cost" : "Стоимость услуг за единицу измерения"
		}

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = ["name", "position", "salary", "tax_rate"]
		labels = {
			"name" : "ФИО сотрудника",
			"position" : "Должность",
			"salary" : "Заработная плата за месяц",
			"tax_rate" : "Расчётная налоговая ставка",
		}