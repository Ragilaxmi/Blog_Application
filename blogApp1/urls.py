
from django.urls import path 
from . import views

urlpatterns=[
    path('',views.display,name='homeurl'),
    path('register/',views.register,name='registerurl'),
    path('loginpage/',views.loginpage,name='loginurl'),
    path('logoutpage/',views.logoutpage,name='logouturl'),
    path('insert/',views.addblog,name='inserturl')
]