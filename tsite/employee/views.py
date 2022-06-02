from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmployeeForm,JobForm,WorkerForm
from .models import Employee,Job,Worker

# Create your views here.
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            Employee.objects.create(**form.cleaned_data)
            #print(form.cleaned_data)
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html',{'form':form,
                                                         'employees':Employee.objects.all(),})

def add_job(request):
    if request.method =='POST':
        form = JobForm(request.POST)
        if form.is_valid():
            Job.objects.create(**form.cleaned_data)
    else:
        form = JobForm()
    return render(request,'employee/add_job.html', {'form':form,
                                                    'jobs':Job.objects.all(),})

def add_worker(request):
    if request.method =='POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            Worker.objects.create(**form.cleaned_data)
    else:
        form = WorkerForm()
    return render(request,'employee/add_worker.html', {'form':form,
                                                    'workers':Worker.objects.all(),})
def delete_job(request,job_id=None):
    job_to_delete = Job.objects.get(id=job_id)
    job_to_delete.delete()
    return HttpResponseRedirect('../add_job')
def delete_employee(request,employee_id = None):
    employee_to_delete = Employee.objects.get(id = employee_id)
    employee_to_delete.delete()
    return HttpResponseRedirect('../add_employee')
def delete_worker(request,worker_id=None):
    worker_to_delete = Worker.objects.get(id = worker_id)
    worker_to_delete.delete()
    return HttpResponseRedirect('../add_worker')