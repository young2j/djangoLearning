from django.contrib import admin

from typeidea.custom_site import custom_site
from .models import Comment

import xadmin

# Register your models here.

# @admin.register(Comment, site=custom_site)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('target', 'nickname', 'content', 'website', 'created_time')

@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')