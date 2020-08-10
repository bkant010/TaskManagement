"""taskmanagementapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from taskapp.views import home,delete_project,edit_project,detail_project,edit_task,delete_task,detail_task,create_project,create_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='index'),
    path('createproject', create_project),
    path('project/delete/<int:id>', delete_project),
    path('project/edit/<int:id>', edit_project),
    path('project/detail/<int:id>', detail_project),
    path('project/<int:p_id>/createtask', create_task),
    path('project/<int:p_id>/task/edit/<int:t_id>', edit_task),
    path('project/<int:p_id>/task/delete/<int:t_id>', delete_task),
    path('project/<int:p_id>/task/detail/<int:t_id>', detail_task),
    path('taskapi/', include('taskapi.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
