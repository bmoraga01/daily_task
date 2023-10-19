from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.utils import timezone

@method_decorator(login_required, name='dispatch')
class DailyTaskList(ListView):
    model = DailyTask
    template_name = 'daily-tasks/list.html'
    
    def get_queryset(self):
        today = timezone.now().date()
        return DailyTask.objects.filter(user=self.request.user, limit_date__gte=today)
    
@method_decorator(login_required, name='dispatch')
class HistoricalDailyTaskList(ListView):
    model = DailyTask
    template_name = 'daily-tasks/historical_list.html'
    
    def get_queryset(self):
        today = timezone.now().date()
        return DailyTask.objects.filter(user=self.request.user, limit_date__lt=today)
    
    
@method_decorator(login_required, name='dispatch')
class CreateDailyTask(CreateView):
    model = DailyTask
    template_name = 'daily-tasks/create.html'
    form_class = DailyTaskForm
    
    def form_valid(self, form):
        if form.is_valid():
            f = form.save(commit=False)
            f.user = self.request.user
            f.save()
        return super(CreateDailyTask, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:dailytask_list')
    
@login_required
def complete_task(request, pk):
    today = timezone.now().date()
    try:
        task = DailyTask.objects.get(pk=pk, user=request.user)
        
        if today <= task.limit_date:
            task.completed = True
            task.completed_date = timezone.now()
            task.save()
        else:
            # you can't complete this task
            pass
    except:
        raise Http404()
    
    return redirect('tasks:dailytask_list')

@login_required
def get_dailytask_detail(request, pk):
    try:
        task = DailyTask.objects.get(pk=pk, user=request.user)
        
        date = task.completed_date.date() if task.completed_date else None
        
        data = {
            'name': task.name,
            'description': task.description,
            'completed': task.completed,
            'completed_date': date,
            'limit_date': task.limit_date,
        }
    except:
        data = {
            'error': 'error'
        }
    
    
    return JsonResponse(data)