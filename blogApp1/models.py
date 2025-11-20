from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    role_name=models.CharField(max_length=300)
    
    def __str__(self):
        return self.role_name

'''
class CustomUser(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=300)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)'''

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in user
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    profile_pic=models.ImageField(upload_to='images/',null=True ,default='images/defimg.jpg')

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    image=models.ImageField(upload_to='images/',null=True,default='images/default.jpg')
    title=models.CharField(max_length=300)
    content=models.TextField()
    author=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog=models.ForeignKey(Blog, null=True,on_delete=models.SET_NULL)
    commenter=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL)
    comment_text=models.TextField()
    commented_on=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"Comment on {self.blog.title}"