from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from JDBC.models import Student
from JDBC.models import Subject
from JDBC.models import MarksObtained
from JDBC.models import sresult
from JDBC.forms import Sforms
from .import models
from django.db.models import Count
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import auth
from JDBC.models import AuthUser
from django.contrib.auth import authenticate
from operator import itemgetter
from django.db import connection
from django.db import transaction
import json
# Create your views here.
def jb(request):
    if request.method=="POST":
        if 'mark' in request.POST:
            eno=request.POST.get('mar')
            return render(request,'marks.html',{"d":eno})
        if 'shw' in request.POST:
            eno=request.POST.get('show')
            return render(request,'one.html',{"db":eno})
    else:
        show=Student.objects.all()
        return render(request, 'jb.html',{"data":show})
def insert(request):
    if request.method=="POST":
        if request.POST.get('student_name') and request.POST.get('father_name') and request.POST.get('mother_name') and request.POST.get('address') and request.POST.get('eno') and request.POST.get('bdate') and request.POST.get('email') and request.POST.get('gender') and request.POST.get('dno'):
            saverecord=Student()
            saverecord.student_name=request.POST.get('student_name')
            saverecord.father_name=request.POST.get('father_name')
            saverecord.mother_name=request.POST.get('mother_name')
            saverecord.address=request.POST.get('address')
            saverecord.eno=request.POST.get('eno')
            saverecord.bdate=request.POST.get('bdate')
            saverecord.email=request.POST.get('email')
            #saverecord.rno=request.POST.get('rno')
            saverecord.gender=request.POST.get('gender')
            saverecord.dno=request.POST.get('dno')
            saverecord.save()
            messages.success(request,'Student'+saverecord.student_name+'is Saved Successfully..!')
            return render(request,'insert.html')
    
    else:
        return render(request,'insert.html')
def edit(request,id):
    editobj=Student.objects.get(id=id)
    return render(request,'edit.html',{"Student":editobj})
def update(request,id):
    upd=Student.objects.get(id=id)
    form=Sforms(request.POST,instance=upd)
    if form.is_valid():
        form.save()
        messages.success(request,'Updated succesfully')
        return render(request,'edit.html',{"Student":upd})
def sub(request):
    form=models.Subject.objects.all()
    return render(request,'sub.html',{"sub":form})

def dele(request,id):
    dele=Student.objects.get(id=id)
    dele.delete()
    showd=Student.objects.all()
    return render(request,'jb.html',{"data":showd})
def delt(request,id):
    de=MarksObtained.objects.get(id=id)
    de.delete()
    av=MarksObtained.objects.all()
    return render(request,'one.html',{"da":av})
def result(request):
    #me=MarksObtained.objects.values('eno','sem').annotate(my_count=Count('id'))
    # r = MarksObtained.objects.values('eno','sem').annotate(Sum("credit_points"),Sum("credit_total"))
    # li=[]
    # for i in r:
    #    # print(i['credit_points__sum'] /i['credit_total__sum'])
    #     li.append(i['credit_points__sum'] /i['credit_total__sum'])
    #     i['SGPA']=round(i['credit_points__sum'] /i['credit_total__sum'],2)
    #     print(li)
    # print(r)
    if request.method=="POST":
        if 'reslt' in request.POST:
            eno=request.POST.get('resu')
            r = MarksObtained.objects.values('eno','sem').annotate(Sum("credit_points"),Sum("credit_total"))
            r=list(r)
            newlist = sorted(r, key=itemgetter('sem'))
            li=[]
            l=[]
            s=0
            j=1
            ab=()
            cursor=connection.cursor()
            cursor.execute("delete from sresult where eno='" + eno+"'")
            for i in newlist:
                if eno == i['eno']:
                    li.append(i['credit_points__sum'] /i['credit_total__sum'])
                    i['SGPA']=round(i['credit_points__sum'] /i['credit_total__sum'],2)
                    i['SA']=(i['credit_points__sum'] /i['credit_total__sum'])
                    s=(s+i['SGPA'])
                    #s=(s+i['SA'])
                    i['OGPA']=round(s/j,2)
                    #j=j+1
                    print(j,i['SA'],i['OGPA'])
                    #print(s)
                    l.append(i['SGPA'])
                    j=j+1
                    ab=sresult(eno=i['eno'],sem=i['sem'],sgpa=i['SGPA'],ogpa=i['OGPA'])
                    ab.save()

            
            return render(request,'result.html',{"E":newlist,"EN":eno})
    else:
        return HttpResponse('404')
def one(request):
   # showall=MarksObtained.objects.all()
    if request.method=="POST":
        if 'shw' in request.POST:
            eno=request.POST.get('show')
            sh=MarksObtained.objects.filter(eno=eno)
            #print(sh[0].course_no)
            return render(request,'one.html',{"E":sh})
        else:
            return HttpResponse('404')
   # return render(request, 'one.html',{"da":showall})
def marks(request):
    if request.method=="POST":
        roll_no=request.POST.get('roll_no')
        batch=request.POST.get('batch')
        sem=request.POST.get('sem')
        eno=request.POST.get('Enrollment Number')
        #sem = Subject.objects.get(sem_no = sem)
        course_no=request.POST.get('course_no')
        course_no=str(course_no)
        course_no = Subject.objects.get(course_code = course_no)
        credit_total=request.POST.get('credit_total')
        midterm_marks=request.POST.get('midterm_marks')
        theory_marks=request.POST.get('theory_marks')
        practical_marks=request.POST.get('practical_marks')
        
        sem=int(sem)
        credit_total=int(credit_total)
        midterm_marks=int(midterm_marks)
        theory_marks=int(theory_marks)
        practical_marks=int(practical_marks)
        grade_point=sm(midterm_marks,theory_marks,practical_marks)
        grade_point=float(grade_point)
        credit_points=cal(credit_total,grade_point)
        credit_points=float(credit_points)
        print(grade_point,credit_points)
        #credit_points=int(credit_points)
        #grade_point=int(sum(midterm_marks+practical_marks+theory_marks))
        ab=MarksObtained(roll_no=roll_no,batch=batch,sem=sem,eno=eno,course_no=course_no,credit_total=credit_total,midterm_marks=midterm_marks,theory_marks=theory_marks,practical_marks=practical_marks,grade_point=grade_point,credit_points=credit_points)
        ab.save()
        messages.success(request,'Saved Successfully')
        return render(request,"marks.html")
    
        
    else:
        return render(request,"marks.html")
def sm(x,y,z):
    sum=x+y+z
    sum=sum/10
    return sum

def cal(a,c):
    count=a*c
    return count
def a(a,b):
    sum=a+b
    return sum
def div(a,b):
    sum=float(a/b)
    return sum

def login(request):
    if request.method == 'POST':
        # user=auth.authenticate(email=request.POST['email'],password=request.POST['password'])
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('jb')
        li=[]
        email=request.POST['email']
        password=request.POST['password']
        cursor=connection.cursor()
        cursor.execute("select email,password from auth_user")
        print(cursor)
        for i in cursor:
            li.append(i)
        print(li)
        flag=0
        for e,p in li:
            if email == e and password == p:
                flag = 1
                break
        if flag == 1:
            return redirect('jb')
        else:
            return render(request,'login.html',{'error':'username or password is invalid'})

    else:
        return render(request,'login.html')
def logout(request):
    return redirect('login')
    