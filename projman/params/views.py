from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import ParamForm
from projman.core.models import Company

# Create your views here.

@login_required
def params(request: HttpRequest):
	if not Company.objects.first():
		field = Company()
		field.save()

	if request.method == "POST":
		form = ParamForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = ParamForm(instance=Company.objects.first())
	else:
		form = ParamForm(instance=Company.objects.first())

	return render(request, "params.html", {"form" : form})