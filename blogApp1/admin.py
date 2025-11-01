from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import User,Role,Blog,Comment
class RoleAdmin(admin.ModelAdmin):
    list_display=['id','role_name']

class UserAdmin(admin.ModelAdmin):
    list_display=['id','email','password','role']

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','content','author','created_on']

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','blog','commenter','comment_text','commented_on']

admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)

