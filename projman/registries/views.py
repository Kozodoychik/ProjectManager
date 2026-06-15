from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponseBadRequest, HttpResponseNotFound
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

	return render(request, "create.html", {"reg_name" : "Заказчики", "action_name" : "Создать", "form" : form, "message" : message})

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

	return render(request, "create.html", {"reg_name" : "Исполнители", "action_name" : "Создать", "form" : form, "message" : message})

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
		
	return render(request, "create.html", {"reg_name" : "Оборудование", "action_name" : "Создать", "form" : form, "message" : message})

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
		
	return render(request, "create.html", {"reg_name" : "Сотрудники", "action_name" : "Создать", "form" : form, "message" : message})

@login_required
def customers_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()

	ids = json.loads(request.POST["ids"])
	Customers.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/customers");

@login_required
def executors_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Executors.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/executors");

@login_required
def hardware_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Hardware.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/hardware");

@login_required
def staff_delete(request: HttpRequest):
	if request.method != "POST" or not "ids" in request.POST:
		return HttpResponseBadRequest()
	
	ids = json.loads(request.POST["ids"])
	Staff.objects.filter(id__in=ids).delete()

	return HttpResponseRedirect("/staff");

@login_required
def customers_edit(request: HttpRequest, id: int):
	message = None

	customer = Customers.objects.filter(id=id)
	if len(customer) == 0: return HttpResponseNotFound()

	form = CustomerForm(instance=customer[0])

	if request.method == "POST":
		form = CustomerForm(request.POST, instance=customer[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/customers")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "create.html", {"reg_name" : "Заказчики", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def executors_edit(request: HttpRequest, id: int):
	message = None

	executor = Executors.objects.filter(id=id)
	if len(executor) == 0: return HttpResponseNotFound()

	form = ExecutorForm(instance=executor[0])

	if request.method == "POST":
		form = ExecutorForm(request.POST, instance=executor[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/executors")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "create.html", {"reg_name" : "Исполнители", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def hardware_edit(request: HttpRequest, id: int):
	message = None

	device = Hardware.objects.filter(id=id)
	if len(device) == 0: return HttpResponseNotFound()

	form = DeviceForm(instance=device[0])

	if request.method == "POST":
		form = DeviceForm(request.POST, instance=device[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/hardware")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "create.html", {"reg_name" : "Оборудование", "action_name" : "Изменить", "form" : form, "message" : message})

@login_required
def staff_edit(request: HttpRequest, id: int):
	message = None

	employee = Staff.objects.filter(id=id)
	if len(employee) == 0: return HttpResponseNotFound()

	form = EmployeeForm(instance=employee[0])

	if request.method == "POST":
		form = EmployeeForm(request.POST, instance=employee[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/staff")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "create.html", {"reg_name" : "Сотрудники", "action_name" : "Изменить", "form" : form, "message" : message})