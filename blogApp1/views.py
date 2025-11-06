from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Role,CustomUser,Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model

from django.contrib.auth.decorators import login_required
User=get_user_model()

# Create your views here.
@login_required(login_url='loginurl')
def display(request):
    return render(request,'base.html')

def register(request):
    if request.method=='GET':
        roles=Role.objects.all()
        return render(request,'blogapp1/register.html',{'roles':roles})
    if request.method=='POST':
        print(request.POST)
        name=request.POST['nme']
        email=request.POST['mail']
        password=request.POST['pwd']
        role=int(request.POST['role'])
        
        r=Role.objects.get(id=role)
        print(r)
        obj=User.objects.create_user(username=name,email=email,password=password)
        u=User.objects.get(email=email)

        uobj=CustomUser.objects.create(role_id=r,user_id=u)
        return redirect('homeurl')

def loginpage(request):
    if request.method=='GET':
        return render(request,'blogapp1/login.html')
    if request.method=='POST':
        uname=request.POST['nme']
        pwd=request.POST['pwd']
        uobj=authenticate(request, username=uname, password=pwd)
        if uobj is None:
            return redirect('loginurl')
        else:
            login(request,uobj)
            return redirect('homeurl')

def logoutpage(request):
    logout(request)
    return redirect('loginurl')

def addblog(request):
    if request.method=='GET':
        
        return render(request,'blogapp1/insert.html')
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        author=CustomUser.objects.get(user=request.user)
        print(title,content,author)
        
