from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Workspace
from .forms import WorkspaceForm

# Create your views here.
@login_required
def workspace(request):
	return render(request, "workspace.html", {"workspaces" : Workspace.objects.all()})

@login_required
def workspace_create(request: HttpRequest):
	return render(request, "create_workspace.html", {"form" : WorkspaceForm(), "reg_name" : "Рабочие области", "action_name" : "Создать"})

@login_required
def workspace_edit(request, slug):
	pass

@login_required
def workspace_delete(request, slug):
	pass