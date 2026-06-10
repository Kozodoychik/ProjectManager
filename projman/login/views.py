from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def login_view(request: HttpRequest):
	if request.user.is_authenticated:
		return HttpResponseRedirect("/")

	message = ""
	if request.method == "POST":
		login_data = LoginForm(request.POST)
		user = authenticate(request, username=login_data.data["email"], password=login_data.data["password"])
		if user:
			login(request, user)
			return HttpResponseRedirect(request.POST["next"] or "/")
		else:
			message = 'Неправильный адрес эл. почты или пароль'

	return render(
		request,
		"login.html", 
		{
			"form" : LoginForm({"email":request.POST.get("email") or "", "password" : ""}), 
			"next" : request.GET.get("next") or "/",
			"message" : message
		}
	)

@login_required
def logout_view(request: HttpRequest):
	logout(request)
	return HttpResponseRedirect("/login")