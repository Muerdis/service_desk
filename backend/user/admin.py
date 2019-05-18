from django.contrib import admin

from user.models import User, Department, Invite

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Invite)
