from django.db import models
from django.utils.translation import gettext_lazy

class Customers(models.Model):
	class CustomerType(models.IntegerChoices):
		NATURAL_PERSON 	= 0, gettext_lazy("Физическое лицо")
		INDIVIDUAL_ENT 	= 1, gettext_lazy("Индивидуальный предприниматель")
		LEGAL_PERSON 	= 2, gettext_lazy("Юридическое лицо")

	inn = models.CharField(max_length=12, unique=True)
	customer_type = models.IntegerField(choices=CustomerType.choices, default=CustomerType.NATURAL_PERSON)
	name = models.CharField(max_length=255, blank=True)
	customer_name = models.CharField(max_length=255)
	contact_email = models.EmailField(max_length=255)
	contact_number = models.CharField(max_length=255)

	def get_type(self):
		return self.CustomerType(self.customer_type).label

class Executors(models.Model):
	class RegistrationType(models.IntegerChoices):
		GPH = 0, gettext_lazy("ГПХ")
		NPD = 1, gettext_lazy("НПД")

	class Units(models.IntegerChoices):
		HOURS	= 0, gettext_lazy("Часы")
		DAYS	= 1, gettext_lazy("Дни")
		FULL	= 2, gettext_lazy("Полная стоимость")

	name = models.CharField(max_length=255)
	registration_type = models.IntegerField(choices=RegistrationType, default=RegistrationType.GPH)
	tax_rate = models.IntegerField()
	unit = models.IntegerField(choices=Units, default=Units.HOURS)
	unit_cost = models.IntegerField()

	def get_registration_type(self):
		return self.RegistrationType(self.registration_type).label
	
	def get_unit(self):
		return self.Units(self.unit).label

class Hardware(models.Model):
	class PurchaseType(models.IntegerChoices):
		OWN		= 0, gettext_lazy("Собственное")
		RENT	= 1, gettext_lazy("В аренде")

	class Units(models.IntegerChoices):
		HOURS	= 0, gettext_lazy("Часы")
		DAYS	= 1, gettext_lazy("Дни")
		FULL	= 2, gettext_lazy("Полная стоимость")

	name = models.CharField(max_length=255)
	description = models.CharField(max_length=1024)
	purchase_type = models.IntegerField(choices=PurchaseType, default=PurchaseType.OWN)
	operating_cost = models.IntegerField()
	unit = models.IntegerField(choices=Units, default=Units.HOURS)
	unit_cost = models.IntegerField()

	def get_purchase_type(self):
		return self.PurchaseType(self.purchase_type).label

	def get_unit(self):
		return self.Units(self.unit).label
	
class Staff(models.Model):
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	salary = models.IntegerField()
	tax_rate = models.IntegerField()