from django.contrib import admin
from .models import Projects, Tasks

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name','description','start_time','end_time','avatar']

class TasksAdmin(admin.ModelAdmin):
    list_display = ['projects','name','description','start_time','end_time']

admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Tasks,TasksAdmin)