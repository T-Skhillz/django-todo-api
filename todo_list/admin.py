from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ["completed", "created_on", "category"]
    search_fields = ["title", "category"]

admin.site.register(Task, TaskAdmin)
