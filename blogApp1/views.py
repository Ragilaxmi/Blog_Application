from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Role,CustomUser,Blog,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model

from django.contrib.auth.decorators import login_required
User=get_user_model()

# Create your views here.
@login_required(login_url='loginurl')
def display(request):
    #return render(request,'base.html')
    if request.method=='GET':
        blog=Blog.objects.order_by('-created_on')
        return render(request,'blogapp1/display.html',{'blog':blog})

def register(request):
    if request.method=='GET':
        roles=Role.objects.all()
        return render(request,'blogapp1/register.html',{'roles':roles})
    if request.method=='POST':
        print(request.POST)
        pic=request.FILES['pic']
        name=request.POST['nme']
        email=request.POST['mail']
        password=request.POST['pwd']
        role_id=request.POST['role']
        
        r=Role.objects.get(id=role_id)
        print(r)
        u=User.objects.create_user(username=name,email=email,password=password)
        #u=User.objects.get(email=email)

        CustomUser.objects.create(role=r,user=u,profile_pic=pic)
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
        img=request.FILES['image']
        try:
            cust_user=CustomUser.objects.get(user=request.user)
            
        except CustomUser.DoesNotExist:
            default_role=Role.objects.first()
            cust_user=CustomUser.objects.create(user=request.user,role=default_role)
        
        Blog.objects.create(title=title,content=content,author=cust_user,image=img)
        return redirect('homeurl')

    
def read(request,bno):
    blog=Blog.objects.get(id=bno)
    if request.method=='GET':
        #blog=Blog.objects.get(id=bno)
        comments=Comment.objects.filter(blog=blog).order_by('-commented_on')
        return render(request,'blogapp1/read.html',{'blog':blog,'comments':comments})
def comment(request,bno):
    blog=Blog.objects.get(id=bno)
    if request.method=='POST':
        comment=request.POST['comment_text']
        custno=CustomUser.objects.get(user_id=request.user.id)
        Comment.objects.create(blog=blog,commenter=custno,comment_text=comment)
        comments=Comment.objects.filter(blog=blog).order_by('-commented_on')

        return render(request,'blogapp1/read.html',{'blog':blog,'comments':comments})
        
        
def searchblog(request):
    query=""
    blogs=[]
    if request.method=="POST":
        query=request.POST.get('search','').strip()
        if query:
            blogs=Blog.objects.filter(title__icontains=query).order_by('-created_on')
            #print(blogs)
        return render(request,'blogapp1/search.html',{'blogs':blogs,'query':query})
        #return HttpResponse('bllog recived')