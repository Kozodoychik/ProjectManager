from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound
from .forms import ProjectForm
from .models import *
import json

# Create your views here.
@login_required
def project_edit(request: HttpRequest, workspace_slug, project_id):
	if not Workspace.objects.filter(slug=workspace_slug): return HttpResponseNotFound()
	workspace = Workspace.objects.filter(slug=workspace_slug)[0]

	if not Project.objects.filter(id=project_id): return HttpResponseNotFound()
	project = Project.objects.filter(id=project_id)[0]

	if project.workspace.slug != workspace.slug: return HttpResponseNotFound()

	form = ProjectForm(instance=project)
	message = None

	if request.method == "POST":
		form = ProjectForm(request.POST, instance=project)

		if form.is_valid():
			form.save()
			return redirect(f"/{workspace_slug}")
		else:
			message = "Проверьте правильность введённых данных"

	return render(request, "form-base.html", {"form" : form, "reg_name" : project.name, "action_name" : "Изменить", "message" : message})

@login_required
def project_delete(request: HttpRequest, workspace_slug, project_id):
	if not Workspace.objects.filter(slug=workspace_slug): return HttpResponseNotFound()
	workspace = Workspace.objects.filter(slug=workspace_slug)[0]

	if not Project.objects.filter(id=project_id): return HttpResponseNotFound()
	project = Project.objects.filter(id=project_id)[0]

	if project.workspace.slug != workspace.slug: return HttpResponseNotFound()

	project.delete()

	return redirect(f"/{workspace_slug}")

@login_required
def projects_bulk_delete(request: HttpRequest, workspace_slug):
	if not Workspace.objects.filter(slug=workspace_slug): return HttpResponseNotFound()
	workspace = Workspace.objects.filter(slug=workspace_slug)[0]
	workspace_project_ids = list(workspace.workspace_projects.all().values_list("id", flat=True))

	ids = json.loads(request.POST["ids"])

	for project_id in ids:
		print(project_id)
		if not project_id in workspace_project_ids:
			return HttpResponseNotFound()
		
	Project.objects.filter(id__in=ids).delete()

	return redirect(f"/{workspace_slug}")