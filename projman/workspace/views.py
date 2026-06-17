from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from projman.projects.forms import ProjectForm
from .models import *
from .forms import WorkspaceForm
from .utils import can_manage_projects

@login_required
def workspace(request):
	return render(request, "workspace.html", {"workspaces" : Workspace.objects.filter()})

@login_required
def workspace_create(request: HttpRequest):
	form = WorkspaceForm()
	message = None

	if request.method == "POST":
		form = WorkspaceForm(request.POST)

		if form.is_valid():
			workspace = form.save(commit=False)
			workspace.admin = request.user
			workspace.save()

			return HttpResponseRedirect("/")
		message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"form" : form, "reg_name" : "Рабочие области", "action_name" : "Создать", "message" : message})

@login_required
def workspace_edit(request, slug):
	message = None
	workspace = get_object_or_404(Workspace, slug=slug)

	form = WorkspaceForm(instance=workspace)

	if request.method == "POST":
		form = WorkspaceForm(request.POST, instance=workspace)

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
	workspace = get_object_or_404(Workspace, slug=slug)
	
	projects = workspace.workspace_projects.all()

	return render(request, "projects.html", {"workspace_name" : workspace.name, "projects" : projects})

@login_required
def workspace_project_create(request: HttpRequest, slug):
	if not can_manage_projects(request, slug): return HttpResponseForbidden()

	message = None
	workspace = get_object_or_404(Workspace, slug=slug)

	form = ProjectForm(request.POST)

	if request.method == "POST":
		form = ProjectForm(request.POST)
		print(request.POST)

		if form.is_valid():
			project = form.save(commit=False)
			project.workspace = workspace
			project.save()

			return HttpResponseRedirect(f"/{slug}")
		message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"form" : form, "reg_name" : f"{workspace.name}", "action_name" : "Создать проект", "message" : message});