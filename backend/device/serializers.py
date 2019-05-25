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

    class Meta:
        model = Device
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    """Сериализатор для обслуживания/бронирования"""

    class Meta:
        model = Reservation
        fields = '__all__'
