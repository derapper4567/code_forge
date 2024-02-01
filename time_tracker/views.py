from django.shortcuts import render, redirect
from .models import Project, Task, TimeEntry
from .forms import ProjectForm, TaskForm, TimeEntryForm

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project.html', {'form': form})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def time_entry_create(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_entry_list')
    else:
        form = TimeEntryForm()
    return render(request, 'time_entry.html', {'form': form})

def save_time(request,project_id):
    if request.method =='POST':
        project=Project.objects.get(id=project_id)
        time_entries = TimeEntry.objects.filter(project=project)

        total_time=sum(entry.get_duration() for entry in time_entries)

        if total_time <=project.max_allowed:
            return redirect('success_page')
        else:
            return redirect('reject_page')

def home(request):
    return render(request=request,template_name=home.html)