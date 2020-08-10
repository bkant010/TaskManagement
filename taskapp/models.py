from django.db import models
import time

# Create your models here.
def project_image_store(instance, filename):
    name = filename.split('.')[0]+"_"+time.strftime('%d-%m-%Y')+"."+filename.split('.')[1]
    return '/'.join(["Projects", name])

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # avatar = models.ImageField()
    avatar = models.ImageField(upload_to=project_image_store)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    projects =models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True,related_name='task_by_project')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # avatar = models.ImageField()
