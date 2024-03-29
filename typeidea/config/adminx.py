from django.contrib import admin
from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.BaseModelAdmin import BaseModelAdmin

import xadmin

# Register your models here.
# @admin.register(Link,site=custom_site)
@xadmin.sites.register(Link)
class LinkAdmin(BaseModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')



# @admin.register(SideBar,site=custom_site)
@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(SideBarAdmin, self).save_model(request, obj, form, change)
