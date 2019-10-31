from django.contrib import admin
from webapp.models import Task, Type, Status, Project
from accounts.models import Git


class TodolistAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at', 'project']
    list_filter = ['summary']
    list_display_links = ['pk', 'description']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'type', 'status', 'created_at', 'project', 'updated_at']
    readonly_fields = ['created_at']



admin.site.register(Task, TodolistAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Git)
