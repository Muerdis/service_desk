from django.contrib import admin

from device.models import DeviceTemplate, Device

admin.site.register(DeviceTemplate)
admin.site.register(Device)
