from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import school





def home(request):

    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        uname=request.POST['username']

        password=request.POST['password']
        cpassword=request.POST['cpassword']
        try:
            if password==cpassword:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,'username already taken')
                    return redirect('/register')

                else:
                    user=User.objects.create_user(username=uname,password=password)
                    user.save()
                    return redirect('/login')
            else:
                messages.info(request,'password mismatch')
                return redirect('/register')
        except:
            messages.info(request,'enter the details ')
    return render(request,'reg.html')
def login(request):
    if request.method=='POST':
        uname = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'please check username and password')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        dob = request.POST.get('dob',)
        age=request.POST.get('age',)
        genderm = request.POST.get('gender',)
        phone = request.POST.get('phone', )
        mail = request.POST.get('mail', )
        dept = request.POST.get('dept', )
        course = request.POST.get('course', )
        # pen=request.POST.get('pen',)
        # a=request.POST.get('a',)
        mv=school(name=name,dob=dob,age=age,gender=genderm,phone=phone,mail=mail,dept=dept,course=course)
        mv.save()
        return render(request,'add.html',{'dept':dept,'course':course})
    return render(request,'add.html')

