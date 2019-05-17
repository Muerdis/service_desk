from django.contrib import admin

from device.models import DeviceTemplate, Device, Reservation

admin.site.register(DeviceTemplate)
admin.site.register(Device)
admin.site.register(Reservation)
