from django.contrib import admin
from .models import *

@admin.register(DailyTask)
class DailyTaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'user']