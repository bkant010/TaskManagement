from django.shortcuts import render
from rest_framework import viewsets
from taskapp.models import Projects,Tasks
from .serializers import Projects_Serializer,Tasks_Serializer
from .filters import Projects_Filter,Tasks_Filter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class Projects_ViewSet(viewsets.ModelViewSet):
    # pdb.set_trace()
    queryset =Projects.objects.all()
    serializer_class =Projects_Serializer
    filter_class = Projects_Filter
    filter_fields = ('id', 'name')

class Tasks_ViewSet(viewsets.ModelViewSet):
    # pdb.set_trace()
    queryset =Tasks.objects.all()
    serializer_class =Tasks_Serializer
    filter_class = Tasks_Filter
    filter_fields = ('id', 'projects__name', 'name')
