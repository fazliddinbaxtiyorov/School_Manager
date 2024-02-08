from django.contrib import admin

from .models import News, StudentsAchievement, Teachers, Students
# Register your models here.

admin.site.register(News)
admin.site.register(StudentsAchievement)
admin.site.register(Teachers)
admin.site.register(Students)
