from django.contrib import admin

from request.models import RequestType, Request, RequestReason, Comment

admin.site.register(RequestReason)
admin.site.register(RequestType)
admin.site.register(Request)
admin.site.register(Comment)
