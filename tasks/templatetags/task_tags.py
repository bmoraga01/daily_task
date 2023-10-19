from django.template import Library
from ..models import *
from datetime import datetime

register = Library()

@register.simple_tag()
def validate_state_task(pk):
    task = DailyTask.objects.get(pk=pk)
    
    now = datetime.now().date()
    limit_date = task.limit_date
    # print(now)
    # print(limit_date)
    
    if task.completed:
        return 'success'
    elif now < limit_date:
        return 'primary'
    elif now == limit_date:
        return 'warning'
    elif now > limit_date:
        return 'danger'
    return 'dark'