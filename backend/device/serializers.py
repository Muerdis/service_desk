from django.conf import settings
from rest_framework import serializers

from device.models import DeviceTemplate, Device, Reservation


class DeviceTemplateSerializer(serializers.ModelSerializer):
    """Сериализатор для шаблонов оборудования"""

    class Meta:
        model = DeviceTemplate
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    """Сериализатор для оборудования"""
    res_dates = serializers.SerializerMethodField()

    def validate(self, data):
        for num_template in settings.NUM_TEMPLATES:
            indexes = [i for i, ltr in enumerate(num_template) if ltr == '*']
            num_from_template_list = list(num_template)
            inventory_number_list = list(data['inventory_number'])
            for index in indexes:
                if not inventory_number_list[index].isdigit():
                    raise serializers.ValidationError('Неверный инвентарный номер')

                num_from_template_list[index] = inventory_number_list[index]

            if num_from_template_list == inventory_number_list:
                break

        return data

    @staticmethod
    def get_res_dates(data):
        return data.device_reservations.values_list('from_date', 'to_date')

    class Meta:
        model = Device
        fields = ('id', 'name', 'inventory_number', 'device_template', 'res_dates')


class ReservationSerializer(serializers.ModelSerializer):
    """Сериализатор для обслуживания/бронирования"""
    title = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    @staticmethod
    def get_title(data):
        if data.request:
            return 'Бронирование {}'.format(data.device.inventory_number)

        return 'Обслуживание {}'.format(data.device.inventory_number)

    @staticmethod
    def get_details(data):
        if data.request:
            return 'Оборудование {} забронивароно по заявке № {}<br>{}<br>{}'.format(
                data.device.inventory_number, data.request.id, data.request.title, data.request.text
            )

        return 'Обслуживание оборудования {}'.format(data.device.inventory_number)

    class Meta:
        model = Reservation
        fields = '__all__'
