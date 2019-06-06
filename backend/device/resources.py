from import_export import resources
from import_export.fields import Field

from device.models import Device, Reservation


class DeviceResource(resources.ModelResource):
    name = Field(column_name='Название')
    inventory_number = Field(column_name='Инвентарный номер')
    device_template = Field(column_name='Название шаблона')

    @staticmethod
    def dehydrate_name(obj):
        return obj.name

    @staticmethod
    def dehydrate_inventory_number(obj):
        return obj.inventory_number

    @staticmethod
    def dehydrate_device_template(obj):
        return obj.device_template.name

    class Meta:
        model = Device
        fields = ('id', 'name', 'inventory_number', 'device_template')
        export_order = ('id', 'name', 'inventory_number', 'device_template')


class ReservationResource(resources.ModelResource):
    name = Field(column_name='Название оборудования')
    inventory_number = Field(column_name='Инвентарный номер')
    request = Field(column_name='Номер заявки')

    @staticmethod
    def dehydrate_name(obj):
        return obj.device.name

    @staticmethod
    def dehydrate_inventory_number(obj):
        return obj.device.inventory_number

    @staticmethod
    def dehydrate_request(obj):
        return obj.request.id if obj.request else ''

    class Meta:
        model = Reservation
        fields = ('id', 'name', 'inventory_number', 'request', 'from_date', 'to_date')
        export_order = ('id', 'name', 'inventory_number', 'request', 'from_date', 'to_date')
