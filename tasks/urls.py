from django.urls import path
from .views import *

app_name = "tasks"

urlpatterns = [
    path('tasks/', DailyTaskList.as_view(), name='dailytask_list'),
    path('tasks/historical', HistoricalDailyTaskList.as_view(), name='historical_dailytask_list'),
    path('tasks/create', CreateDailyTask.as_view(), name='create_dalitask'),
    path('tasks/<int:pk>', get_dailytask_detail, name='dailytask_detail'),
    path('tasks/<int:pk>/complete', complete_task, name='complete_task'),
    
]
