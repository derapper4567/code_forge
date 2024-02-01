from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    max_allowed = models.PositiveIntegerField(0)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def get_duration(self):
        duration=self.end_time-self.start_time
        return duration.total_seconds()//60