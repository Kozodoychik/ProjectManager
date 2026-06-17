from django.db import models

# Create your models here.
class Employee(models.Model):
	pos = models.CharField(max_length=255)