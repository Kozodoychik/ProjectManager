from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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


@login_required
def create_customer_view(request: HttpRequest):
	form = CustomerForm()
	message = None

	if request.method == "POST":
		form = CustomerForm(request.POST)
		
		if form.is_valid():
			inn = request.POST["inn"]
			if inn.isnumeric() and (len(inn) == 10 or len(inn) == 12):
				form.save()
				return HttpResponseRedirect("/customers")
			message = "ИНН должен содержать только 12 цифр (для физ. лица и ИП) или 10 цифр (для юр. лица)"
		else:
			errors = form.errors.as_data()
			if "inn" in errors:
				if errors["inn"][0].code == "unique":
					message = "Заказчик с данным ИНН уже существует"

	return render(request, "create.html", {"reg_name" : "Заказчики", "form" : form, "message" : message})

@login_required
def create_executor_view(request: HttpRequest):
	form = ExecutorForm()

	if request.method == "POST":
		form = ExecutorForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/executors")

	return render(request, "create.html", {"reg_name" : "Исполнители", "form" : form})

@login_required
def create_device_view(request):
	form = DeviceForm()

	if request.method == "POST":
		form = DeviceForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/hardware")
		
	return render(request, "create.html", {"reg_name" : "Оборудование", "form" : DeviceForm()})

@login_required
def create_employee_view(request):
	form = EmployeeForm()

	if request.method == "POST":
		form = EmployeeForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/staff")
		
	return render(request, "create.html", {"reg_name" : "Сотрудники", "form" : EmployeeForm()})

@login_required
def customers_action(request: HttpRequest, id):
	pass

@login_required
def executors_action(request: HttpRequest, id):
	pass

@login_required
def hardware_action(request: HttpRequest, id):
	pass

@login_required
def staff_action(request: HttpRequest, id):
	pass