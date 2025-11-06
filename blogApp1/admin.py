from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import CustomUser,Role,Blog,Comment
class RoleAdmin(admin.ModelAdmin):
    list_display=['id','role_name']

#class CustomUserAdmin(admin.ModelAdmin):
    #list_display=['id','role']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_username', 'get_email', 'get_password', 'role']

    # To fetch username from linked User table
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    # To fetch email
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    # To fetch password (hashed)
    def get_password(self, obj):
        return obj.user.password
    get_password.short_description = 'Password (hashed)'

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','content','author','created_on']

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','blog','commenter','comment_text','commented_on']

admin.site.register(Role,RoleAdmin)
#admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)

