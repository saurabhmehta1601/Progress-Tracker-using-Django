from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class MonthlyGoal(models.Model):
    task_title=models.CharField(max_length=70)
    task_detail=models.CharField(max_length=200,null=True)
    deadline=models.DateTimeField(default=timezone.now()+datetime.timedelta(days=30))
    is_done=models.BooleanField(default=False)

    def time_left(self):
        return self.deadline-timezone.now()

    def __str__(self):
        return self.task_title


class WeeklyGoal(models.Model):
    task_title=models.CharField(max_length=70)
    task_detail=models.CharField(max_length=200,null=True)
    deadline=models.DateTimeField(default=timezone.now()+datetime.timedelta(days=7))
    is_done=models.BooleanField(default=False)

    def time_left(self):
        return self.deadline-timezone.now()

    def __str__(self):
        return self.task_title


class DailyGoal(models.Model):
    task_title=models.CharField(max_length=70)
    task_detail=models.CharField(max_length=200,null=True)
    deadline=models.DateTimeField(default=timezone.now()+datetime.timedelta(days=1))
    is_done=models.BooleanField(default=False)

    def time_left(self):
        return self.deadline-timezone.now()

    def __str__(self):
        return self.task_title