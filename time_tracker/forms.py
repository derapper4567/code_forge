from django import forms
from .models import Project
from .models import Task
from .models import TimeEntry

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'assigned_to']
    

class TimeEntryForm(forms.Form):
    class Meta:
        model = TimeEntry
        fields = ['project', 'task', 'start_time', 'end_time']
    