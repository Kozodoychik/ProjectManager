from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=255)
	deadline = models.DateField()
	description = models.CharField(max_length=1024)
	tax_rate = models.IntegerField()