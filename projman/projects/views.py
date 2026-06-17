from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, HttpResponseForbidden
from projman.workspace.utils import can_manage_projects
from .forms import *
from .models import *
import json

def check_and_get_project(workspace_slug, project_id):
	workspace = get_object_or_404(Workspace, slug=workspace_slug)

	project = get_object_or_404(Project, id=project_id)

	if project.workspace.slug != workspace.slug: return None

	return project

# Create your views here.
@login_required
def project_edit(request: HttpRequest, workspace_slug, project_id):
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()

	project = check_and_get_project(workspace_slug, project_id)

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
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()

	project = check_and_get_project(workspace_slug, project_id)

	project.delete()

	return redirect(f"/{workspace_slug}")

@login_required
def projects_bulk_delete(request: HttpRequest, workspace_slug):
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()

	workspace = get_object_or_404(Workspace, slug=workspace_slug)
	workspace_project_ids = list(workspace.workspace_projects.all().values_list("id", flat=True))

	ids = json.loads(request.POST["ids"])

	for project_id in ids:
		print(project_id)
		if not project_id in workspace_project_ids:
			return HttpResponseNotFound()
		
	Project.objects.filter(id__in=ids).delete()

	return redirect(f"/{workspace_slug}")

@login_required
def project_resources(request: HttpRequest, workspace_slug, project_id):
	project = check_and_get_project(workspace_slug, project_id)

	return render(request, "resources.html", {"project_name" : project.name, "resources" : project.resources.all()})

@login_required
def project_resource_add(request: HttpRequest, workspace_slug, project_id):
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()

	project = check_and_get_project(workspace_slug, project_id)

	step = request.GET.get("step")

	if request.method == "POST":
		resource_form = ProjectResourceForm(request.POST)

		if resource_form.is_valid():
			resource = resource_form.save(commit=False)
			resource.project = project

			resource.resource_id = request.POST["resource_id"]
			resource.resource_type = request.POST["resource_type"]

			resource.save()
			return redirect(f"/{workspace_slug}/{project_id}/resources")
		
	elif request.method == "GET" and step:
		resource_type = request.GET.get("resource_type")
		resource_id = request.GET.get("resource_id")

		if (resource_type is None) or (step == "2" and resource_id is None) or (step != "1" and step != "2"):
			return HttpResponseNotFound()
		
	return render(request, "add-resource.html", {
	   "form" : ResourceTypeForm(),
	   "resource_form" : ProjectResourceForm(),
	   "reg_name" : project.name,
	   "action_name" : "Добавить ресурс",
	   "executors" : Executors.objects.all(),
	   "hardware" : Hardware.objects.all(),
	   "staff" : Staff.objects.all()
	})

@login_required
def project_resource_remove(request: HttpRequest, workspace_slug, project_id, resource_id):
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()
	project = check_and_get_project(workspace_slug, project_id)

	resource = get_object_or_404(ProjectResource, id=resource_id)

	resource.delete()

	return redirect(f"/{workspace_slug}/{project_id}/resources")

@login_required
def project_resources_bulk_remove(request: HttpRequest, workspace_slug, project_id):
	if not can_manage_projects(request, workspace_slug): return HttpResponseForbidden()
	
	project = check_and_get_project(workspace_slug, project_id)

	project_resources_ids = list(project.resources.all().values_list("id", flat=True))

	ids = json.loads(request.POST["ids"])

	for resource_id in ids:
		if not resource_id in project_resources_ids:
			return HttpResponseNotFound()
		
	ProjectResource.objects.filter(id__in=ids).delete()

	return redirect(f"/{workspace_slug}/{project_id}/resources")