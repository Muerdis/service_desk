from django.contrib import admin
from import_export.admin import ExportMixin

from device.models import DeviceTemplate, Device, Reservation
from device.resources import DeviceResource, ReservationResource


@admin.register(Device)
class DeviceAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = DeviceResource


@admin.register(Reservation)
class ReservationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ReservationResource


admin.site.register(DeviceTemplate)
