from django.db import models

# Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=300)


class User(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=300)
    role=models.CharField(max_length=300)


class Blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_on=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    blog=models.ForeignKey(Blog, null=True,on_delete=models.SET_NULL)
    commenter=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    comment_text=models.TextField()
    commented_on=models.DateTimeField(auto_now_add=True)