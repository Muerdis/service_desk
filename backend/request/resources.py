from import_export import resources
from import_export.fields import Field

from request.models import Request


class RequestResource(resources.ModelResource):
    title = Field(column_name='Заголовок')
    text = Field(column_name='Текст')
    request_type = Field(column_name='Тип заявки')
    request_reason = Field(column_name='Причина заявки')
    creator_fio = Field(column_name='ФИО создателя')
    creator_email = Field(column_name='Email создателя')
    assigned_fio = Field(column_name='ФИО назначенного')
    assigned_email = Field(column_name='Email назначенного')
    status = Field(column_name='Статус')

    @staticmethod
    def dehydrate_title(obj):
        return obj.title

    @staticmethod
    def dehydrate_text(obj):
        return obj.text

    @staticmethod
    def dehydrate_request_type(obj):
        return obj.request_reason.request_type.name

    @staticmethod
    def dehydrate_request_reason(obj):
        return obj.request_reason.text

    @staticmethod
    def dehydrate_status(obj):
        return obj.get_status_display()

    @staticmethod
    def dehydrate_creator_fio(obj):
        return obj.created_user.get_full_name()

    @staticmethod
    def dehydrate_creator_email(obj):
        return obj.created_user.email

    @staticmethod
    def dehydrate_assigned_fio(obj):
        return obj.assigned_user.get_full_name()

    @staticmethod
    def dehydrate_assigned_email(obj):
        return obj.assigned_user.email

    class Meta:
        model = Request
        fields = (
            'id', 'title', 'text', 'request_reason', 'request_type', 'status', 'creator_fio',
            'creator_email', 'assigned_fio', 'assigned_email', 'date_created'
        )
        export_order = (
            'id', 'title', 'text', 'request_reason', 'request_type', 'status', 'creator_fio',
            'creator_email', 'assigned_fio', 'assigned_email', 'date_created'
        )
