from django.contrib import admin
from .models import *

# Register your models here.

class WorkspaceUsersInline(admin.TabularInline):
	model = WorkspacePermissions
	extra = 1

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
	inlines = [WorkspaceUsersInline]
	prepopulated_fields = {"slug" : ("name",)}