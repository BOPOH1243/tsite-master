from django import forms
from .models import Employee,Job,Worker

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={"class": "form-control"}))
    name2 = forms.CharField(max_length=150, label='Фамилия', widget=forms.TextInput(attrs={"class": "form-control"}))
    name3 = forms.CharField(max_length=150, label='Отчество', widget=forms.TextInput(attrs={"class": "form-control"}))
    age = forms.IntegerField( label='Возраст', widget=forms.NumberInput(attrs={"class": "form-control"}))
    sex = forms.BooleanField( label='пол(True - мужской)',widget=forms.CheckboxInput(attrs={"class": "form-control"}))

class JobForm(forms.Form):
    title = forms.CharField(max_length=150,label='наименование',widget = forms.TextInput(attrs={"class": "form-control"}))
    category = forms.CharField(max_length=150,label='категория должности',widget = forms.TextInput(attrs={"class": "form-control"}))

class WorkerForm(forms.Form):
    job = forms.ModelChoiceField(empty_label='выберите должность',label='должность',queryset=Job.objects.all())
    employee = forms.ModelChoiceField(empty_label='выберите сотрудника',label='сотрудник',queryset=Employee.objects.all())