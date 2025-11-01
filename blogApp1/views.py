from django.shortcuts import render
from . models import Role
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginurl')
def display(request):
    return render(request,'base.html')

def register(request):
    if request.method=='GET':
        roles=Role.objects.all()
        return render(request,'blogapp1/register.html',{'roles':roles})
    if request.method=='POST':
        pass

def login(request):
    if request.method=='GET':
        return render(request,'blogapp1/login.html')
    
