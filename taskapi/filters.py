
from django_filters import FilterSet

from taskapp.models import Projects,Tasks

class Projects_Filter(FilterSet):
    class Meta:
        model=Projects
        exclude = ('avatar')

        # fields='__all__'

class Tasks_Filter(FilterSet):
    class Meta:
        model=Tasks
        fields='__all__'

