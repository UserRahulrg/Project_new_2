from django.urls import path
from django.shortcuts import HttpResponse,render
from django.urls import include


def biggest_number_in4(request):
    resp=render(request,'biggest_number_in4.html')
    return resp

urlpatterns=[
    path('biggest/',biggest_number_in4),
]


