from django.db import models

class DailyTask(models.Model):
    name            = models.CharField(max_length=170)
    description     = models.TextField(null=True, blank=True)
    completed       = models.BooleanField(default=False)
    completed_date  = models.DateTimeField(null=True, blank=True)
    limit_date      = models.DateField(null=True, blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    user            = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Daily Task'
        verbose_name_plural = 'Daily Tasks'
        
    def __str__(self):
        return 'Daily Tasks from %s'%(self.user)