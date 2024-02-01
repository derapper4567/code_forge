from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='project'),
    path('tasks/', views.task, name='task'),
    path('time-entries/', views.time_entry, name='time_entry'),
]