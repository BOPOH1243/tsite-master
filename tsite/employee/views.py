from django.shortcuts import render
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