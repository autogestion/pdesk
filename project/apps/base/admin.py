
from django.contrib import admin

from project.apps.base.models import RedUser, RedProject, RedVersion, RedTask


class RedUserAdmin(admin.ModelAdmin):
    model = RedUser
    list_display = ('id', 'firstname', 'lastname', 'username', 'email')



class RedProjectAdmin(admin.ModelAdmin):
    model = RedProject
    list_display = ('id', 'title')

class RedVersionAdmin(admin.ModelAdmin):
    model = RedVersion
    list_display = ('id', 'title', 'project')

class RedTaskAdmin(admin.ModelAdmin):
    model = RedTask
    list_display = ('id', 'title', 'project', 'estimated_hours', 'spent_hours', 'author', 'assigned_to', 'version')



admin.site.register(RedUser, RedUserAdmin)
admin.site.register(RedProject, RedProjectAdmin)
admin.site.register(RedVersion, RedVersionAdmin)
admin.site.register(RedTask, RedTaskAdmin)