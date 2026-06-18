from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import json

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
			else:
				message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Заказчики", "action_name" : "Создать", "form" : form, "message" : message})

@login_required
def create_executor_view(request: HttpRequest):
	form = ExecutorForm()
	message = None

	if request.method == "POST":
		form = ExecutorForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/executors")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Исполнители", "action_name" : "Создать", "form" : form, "message" : message})

@login_required
def create_device_view(request):
	form = DeviceForm()
	message = None

	if request.method == "POST":
		form = DeviceForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/hardware")
		else:
			message = "Проверьте правильность введённых данных"
		
	return render(request, "form-base.html", {"reg_name" : "Оборудование", "action_name" : "Создать", "form" : form, "message" : message})

@login_required
def create_employee_view(request):
	form = EmployeeForm()
	message = None

	if request.method == "POST":
		form = EmployeeForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/staff")
		else:
			message = "Проверьте правильность введённых данных"
		
	return render(request, "form-base.html", {"reg_name" : "Сотрудники", "action_name" : "Создать", "form" : form, "message" : message})

@login_required
def customers_bulk_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()

	ids = json.loads(request.POST["ids"])
	Customers.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/customers");

@login_required
def executors_bulk_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Executors.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/executors");

@login_required
def hardware_bulk_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Hardware.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/hardware");

@login_required
def staff_bulk_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Staff.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/staff");

@login_required
def customer_delete(request: HttpRequest, id: int):
	customer = get_object_or_404(Customers, id=id)
	customer.delete()

	return HttpResponseRedirect("/customers")

@login_required
def executor_delete(request: HttpRequest, id: int):
	executor = get_object_or_404(Executors, id=id)
	executor.delete()

	return HttpResponseRedirect("/executors")

@login_required
def device_delete(request: HttpRequest, id: int):
	device = get_object_or_404(Hardware, id=id)
	device.delete()

	return HttpResponseRedirect("/hardware")

@login_required
def employee_delete(request: HttpRequest, id: int):
	employee = get_object_or_404(Staff, id=id)
	employee.delete()

	return HttpResponseRedirect("/staff")

@login_required
def customer_edit(request: HttpRequest, id: int):
	message = None

	customer = get_object_or_404(Customers, id=id)

	form = CustomerForm(instance=customer[0])

	if request.method == "POST":
		form = CustomerForm(request.POST, instance=customer[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/customers")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Заказчики", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def executor_edit(request: HttpRequest, id: int):
	message = None

	executor = get_object_or_404(Executors, id=id)

	form = ExecutorForm(instance=executor)

	if request.method == "POST":
		form = ExecutorForm(request.POST, instance=executor)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/executors")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Исполнители", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def device_edit(request: HttpRequest, id: int):
	message = None

	device = get_object_or_404(Hardware, id=id)

	form = DeviceForm(instance=device)

	if request.method == "POST":
		form = DeviceForm(request.POST, instance=device)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/hardware")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Оборудование", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def employee_edit(request: HttpRequest, id: int):
	message = None

	employee = get_object_or_404(Staff, id=id)

	form = EmployeeForm(instance=employee)

	if request.method == "POST":
		form = EmployeeForm(request.POST, instance=employee)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/staff")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"reg_name" : "Сотрудники", "action_name" : "Изменить", "form" : form, "message" : message})