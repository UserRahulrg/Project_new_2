from django.shortcuts import render
from new_project_app.models import * 
from django.shortcuts import HttpResponse

def new_project_app_home(request):
    if request.method=="GET":
        resp=render(request,'home.html')
        return resp
    elif request.method=="POST":
        if 'btnadd' in request.POST:
            stu=Student()
            stu.userid=request.POST.get('txtuserid',0)
            stu.name=request.POST.get('txtname','NA')
            stu.course=request.POST.get('txtcourse','NA')
            stu.branch=request.POST.get('txtbranch','NA')
            stu.rollno=request.POST.get('txtrollno',0)
            stu.batch=request.POST.get('txtbatch','NA')
            stu.save()
            return HttpResponse("<h1>Student Added Successfully!</h1>")
        elif 'btnsearch' in request.POST:
            eid=int(request.POST.get('searchid_data',0))
            print("eid=",eid)
            stu=Student.objects.get(id=eid)
            d1={'stu': stu}
            resp=render(request,'home.html',context=d1)
            return resp
        elif 'btnshowall' in request.POST:
            stuall=Student.objects.all()
            d1={'Student':stuall}
            resp=render(request,'home.html',context=d1)
            return resp
        elif 'btnmodify' in request.POST:
            stu=Student()
            stu.id=int(request.POST.get('txteid',0))
            if Student.objects.filter(id=stu.id).exists():
                stu.userid=request.POST.get('modify_userid',0)
                stu.name=request.POST.get('modify_name','NA')
                stu.course=request.POST.get('modify_course','NA')
                stu.branch=request.POST.get('modify_branch','NA')
                stu.rollno=request.POST.get('modify_rollno',0)
                stu.batch=request.POST.get('modify_batch',0)
                stu.save()
                return HttpResponse("<h1>Student data modified!</h1>")
            else:
                return HttpResponse("<h1>Student data does not exist!</h1>")
        elif 'btndelete' in request.POST:
            stu=Student()
            stu.id=int(request.POST.get('deleteid_data',0))
            Student.objects.filter(id=stu.id).delete()
            return HttpResponse("<h1>Student data deleted!</h1>")
        else:
            return HttpResponse("<h1>Choose from above options only!</h1>")


def search_student_data(request):
    if request.method=='POST':
        eid=int(request.POST.get('searchid_data',0))
        stu=Student.objects.get(id=eid)
        d1={'stu':stu}
        resp=render(request,'search_student.html',context=d1)
        return resp
    elif request.method=='GET':
        resp=render(request,'search_student.html')
        return resp


def modify_student_data(request):
    if request.method=='GET':
        resp=render(request,'modify_student.html')
        return resp
    elif request.method=='POST':
        stu=Student()
        stu.id=int(request.POST.get('txteid',0))
        if Student.objects.filter(id=stu.id).exists():
            stu.userid=request.POST.get('modify_userid',0)
            stu.name=request.POST.get('modify_name','NA')
            stu.course=request.POST.get('modify_course','NA')
            stu.branch=request.POST.get('modify_branch','NA')
            stu.rollno=request.POST.get('modify_rollno',0)
            stu.batch=request.POST.get('modify_batch',0)
            stu.save()
            return HttpResponse("<h1>Student data modified!</h1>")
        else:
            return HttpResponse("<h1>Student data doesn't exist!</h1>")


def showall_student_data(request):
    if request.method=='GET':
        resp=render(request,'showall_student.html')
        return resp
    elif request.method=='POST':
        stuall=Student.objects.all()
        d1={'Student':stuall}
        resp=render(request,'showall_student.html',context=d1)
        return resp

 
def delete_student_data(request):
    if request.method=='GET':
        resp=render(request,'delete_student.html')
        return resp
    elif request.method=='POST':
        stu=Student()
        stu.id=int(request.POST.get('deleteid_data',0))
        Student.objects.filter(id=stu.id).delete()
        return HttpResponse("<h1>Student data deleted!</h1>")
    


def add_student_data(request):
    if request.method=='GET':
        resp=render(request,'addstudent_data.html')
        return resp
    elif request.method=='POST':
        stu=Student()
        stu.userid=request.POST.get('txtuserid',0)
        stu.name=request.POST.get('txtname','NA')
        stu.course=request.POST.get('txtcourse','NA')
        stu.branch=request.POST.get('txtbranch','NA')
        stu.rollno=request.POST.get('txtrollno',0)
        stu.batch=request.POST.get('txtbatch','NA')
        stu.save()
        return HttpResponse("<h1>Student data added!</h1>")
            

                


            


            

# Create your views here.
