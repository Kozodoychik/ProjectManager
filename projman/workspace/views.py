from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from projman.projects.forms import ProjectForm
from .models import Workspace
from .forms import WorkspaceForm

# Create your views here.
@login_required
def workspace(request):
	return render(request, "workspace.html", {"workspaces" : Workspace.objects.all()})

@login_required
def workspace_create(request: HttpRequest):
	form = WorkspaceForm()
	message = None

	if request.method == "POST":
		form = WorkspaceForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"form" : form, "reg_name" : "Рабочие области", "action_name" : "Создать", "message" : message})

@login_required
def workspace_edit(request, slug):
	message = None
	workspace = Workspace.objects.filter(slug=slug)

	if not workspace: return HttpResponseNotFound()

	form = WorkspaceForm(instance=workspace[0])

	if request.method == "POST":
		form = WorkspaceForm(request.POST, instance=workspace[0])

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		message = "Проверьте правильность введённых данных"

		if Workspace.objects.filter(slug=request.POST["slug"]):
			message = "Рабочая область с таким поддоменом уже существует"
	
	return render(request, "form-base.html", {"form" : form, "reg_name" : "Рабочие области", "action_name" : "Изменить", "message" : message})

@login_required
def workspace_delete(request, slug):
	Workspace.objects.filter(slug=slug).delete()

	return HttpResponseRedirect("/");

@login_required
def workspace_projects(request: HttpRequest, slug):
	workspace = Workspace.objects.filter(slug=slug)

	if not workspace: return HttpResponseNotFound()
	
	projects = workspace[0].workspace_projects.all()

	return render(request, "projects.html", {"workspace_name" : workspace[0].name, "projects" : projects})

@login_required
def workspace_project_create(request: HttpRequest, slug):
	message = None
	workspace = Workspace.objects.filter(slug=slug)

	if not workspace: return HttpResponseNotFound()

	form = ProjectForm(request.POST)

	if request.method == "POST":
		form = ProjectForm(request.POST)
		print(request.POST)

		if form.is_valid():
			project = form.save(commit=False)
			project.workspace = workspace[0]
			project.save()

			return HttpResponseRedirect(f"/{slug}")
		message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"form" : form, "reg_name" : f"{workspace[0].name}", "action_name" : "Создать проект", "message" : message});