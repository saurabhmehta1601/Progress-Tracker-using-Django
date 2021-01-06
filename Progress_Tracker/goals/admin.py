from django.contrib import admin
from .models import MonthlyGoal,WeeklyGoal,DailyGoal
# Register your models here.


admin.site.register(MonthlyGoal)
admin.site.register(WeeklyGoal)
admin.site.register(DailyGoal)
