
from django.urls import path 
from . import views

urlpatterns=[
    path('',views.display),
    path('register/',views.register,name='registerurl'),
    path('login/',views.login,name='loginurl'),
]