from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=255, default="Компания")
	head_name = models.CharField(max_length=255)
	head_pos = models.CharField(max_length=255)
	contact_number = models.CharField(max_length=255)
	contact_email = models.EmailField(max_length=255)

	def save(self, *args, **kwargs):
		self.pk = 1
		super().save(*args, **kwargs)

	@classmethod
	def load(model):
		obj, created = model.objects.get_or_create(pk=1)
		return obj