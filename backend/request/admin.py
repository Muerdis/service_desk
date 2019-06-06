from django.contrib import admin
from import_export.admin import ExportMixin

from request.models import RequestType, Request, RequestReason, Comment
from request.resources import RequestResource


@admin.register(Request)
class RequestAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RequestResource


admin.site.register(RequestReason)
admin.site.register(RequestType)
admin.site.register(Comment)
