from django.contrib import admin
from .models import Employee,Job,Worker

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','name2','name3','sex','age')
admin.site.register(Employee, EmployeeAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','category')
admin.site.register(Job, JobAdmin)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('employee','job')
admin.site.register(Worker,WorkerAdmin)

