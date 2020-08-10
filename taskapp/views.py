from django.shortcuts import render,redirect
from .models import Projects, Tasks
import pdb

def home(request):

    project=Projects.objects.all()
    return render(request,'home.html',{'project':project})

def create_project(request):

    if request.method == 'POST':
        name= request.POST.get("name", "")
        description=request.POST.get("description", "")
        start_time = request.POST.get("start_time", "")
        end_time = request.POST.get("end_time", "")
        avatar = request.FILES.get("avatar", "")

        try:
            proj=Projects(name=name,description=description,start_time=start_time,end_time=end_time,avatar=avatar)
            proj.save()
        except:
            print('Project Insertion error')

    return render(request,'create_project.html')

def delete_project(request,id):
    project=project=Projects.objects.get(id=id)
    project.delete()
    project=Projects.objects.all()
    return render(request, 'home.html', {'project': project})

def edit_project(request,id):
    project = Projects.objects.get(id=id)
    task = Tasks.objects.filter(projects__name=project.name)
    if request.method == 'POST':
        # pdb.set_trace()
        project.name = request.POST.get("name", "")
        project.description=request.POST.get("description", "")
        start_time = request.POST.get("start_time", "")
        if start_time:
            project.start_time=start_time
        end_time = request.POST.get("end_time", "")
        if end_time:
            project.end_time=end_time
        avatar = request.FILES.get("avatar", "")
        if avatar:
            project.avatar=avatar
        project.save()
        return redirect('/')
    return render(request,'edit_project.html', {'project': project,'task': task})

def detail_project(request,id):
    # pdb.set_trace()
    project = Projects.objects.get(id=id)
    task = Tasks.objects.filter(projects__name=project.name)
    return render(request,'Project_details.html', {'project':project,'task': task})

def create_task(request,p_id):
    projects=Projects.objects.all()
    if request.method == 'POST':
        # pdb.set_trace()
        proj = request.POST.get("project", ""),
        project = Projects.objects.get(name__iexact=proj[0])
        name = request.POST.get("name", "")
        description=request.POST.get("description", "")
        start_time = request.POST.get("start_time", "")
        end_time = request.POST.get("end_time", "")
        try:
            # pdb.set_trace()
            task = Tasks(projects=project, name=name,description=description, start_time=start_time, end_time=end_time)
            task.save()
        except :
            print("Databse Insertion Error")
    return render(request,'create_task.html',{'projects':projects})

def edit_task(request,p_id,t_id):
    # pdb.set_trace()
    task = Tasks.objects.get(id=t_id)
    if request.method == 'POST':
        task.name = request.POST.get("name", "")
        task.description=request.POST.get("description", "")
        start_time = request.POST.get("start_time", "")
        if start_time:
            task.start_time = start_time
        end_time = request.POST.get("end_time", "")
        if end_time:
            task.end_time = end_time
        task.save()
        return redirect('/')
    return render(request,'edit_task.html', {'task': task})

def delete_task(request,p_id,t_id):
    task=Tasks.objects.get(id=t_id)
    task.delete()
    project=Projects.objects.get(id=p_id)
    task = Tasks.objects.filter(projects__name=project.name)
    return render(request,'Project_details.html', {'project':project,'task': task})

def detail_task(request,p_id,t_id):
    task = Tasks.objects.get(id=t_id)
    if request.method=='POST':
        return redirect('/')
    return render(request,'task_details.html', {'task': task})

