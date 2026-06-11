from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def customers_view(request):
	return render(request, "customers.html", {"customers" : Customers.objects.all()})

@login_required
def executors_view(request):
	return render(request, "executors.html", {"executors" : Executors.objects.all()})

@login_required
def hardware_view(request):
	return render(request, "hardware.html", {"hardware" : Hardware.objects.all()})

@login_required
def staff_view(request):
	return render(request, "staff.html", {"staff" : Staff.objects.all()})