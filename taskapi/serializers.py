from rest_framework import serializers
from taskapp.models import Projects,Tasks

class Projects_Serializer(serializers.ModelSerializer):

    class Meta:
        model=Projects
        fields=('name','description','start_time','end_time','avatar')

class Tasks_Serializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(
        # queryset=Projects.objects.all(),
        # required=True,
        # source='projects',
        # read_only=True
    # )

    projects = Projects_Serializer(read_only=False,many=True)
    # projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # task_by_project = Projects_Serializer(source='projects',read_only=False)
    class Meta:
        model=Tasks
        fields=('name','description','start_time','end_time','projects')
        # exclude=('projects',)

