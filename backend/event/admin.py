from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from event.models import Event


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )
