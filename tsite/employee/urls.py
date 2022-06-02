from django.urls import path
from .views import *

urlpatterns = [
    path('', add_employee,name='add_employee'),
    path('add_employee/', add_employee,name='add_employee'),
    path('add_job/', add_job, name='add_job'),
    path('add_worker/', add_worker,name='add_worker'),
    path('delete_job/<job_id>',delete_job,name='delete_job'),
    path('delete_worker/<worker_id>',delete_worker,name='delete_worker'),
    path('delete_employee/<employee_id>',delete_employee,name='delete_employee'),
]