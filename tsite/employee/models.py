from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name = "имя")
    name2 = models.CharField(max_length=150, verbose_name = "фамилия")
    name3 = models.CharField(max_length=150, verbose_name = "отчество", blank = True)
    age = models.IntegerField()
    sex = models.BooleanField(verbose_name = "пол (True-мужской)")
    def __str__(self):
        return self.name2+' '+self.name+' '+self.name3

class Job(models.Model):
    title = models.CharField(max_length=150, verbose_name = "наименование")
    category = models.CharField(max_length=150, verbose_name = "категория")
    def __str__(self):
        return self.title+' '+self.category

class Worker(models.Model):
    job = models.ForeignKey("Job", on_delete=models.PROTECT, null=True)
    employee = models.ForeignKey("Employee", on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.job.title+' '+str(self.employee)
#class Workers(models.Model):
