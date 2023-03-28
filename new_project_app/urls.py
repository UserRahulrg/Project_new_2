
from django.urls import path
from django.shortcuts import render
from new_project_app.views import *

def calculator_data_funct(request):
    resp=render(request,'calculator_data.html')
    return resp

def calc_data(request):
    resp=render(request,'calc.html')
    return resp

urlpatterns=[
    path('home/',new_project_app_home),
    path('searchstudent/',search_student_data),
    path('modifystudent/',modify_student_data),
    path('showallstudent/',showall_student_data),
    path('deletestudent/',delete_student_data),
    path('addstudent/',add_student_data),
    path('calculator/',calculator_data_funct),
    path('calc/',calc_data),
    
]


