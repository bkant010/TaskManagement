# from django.contrib import admin
from django.urls import path,include
from .views import Projects_ViewSet,Tasks_ViewSet
from rest_framework import routers
router=routers.DefaultRouter()


router.register('project',Projects_ViewSet)
router.register('task',Tasks_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]