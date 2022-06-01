from django.urls import path
from .views import *

urlpatterns = [
    path('', add_employee,name='add_employee'),
    path('add_employee/', add_employee,name='add_employee'),
    path('add_job/', add_job, name='add_job'),
    path('add_worker/', add_worker,name='add_worker'),
]