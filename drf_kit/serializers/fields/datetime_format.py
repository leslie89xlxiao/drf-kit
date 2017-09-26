from django.utils import timezone

from .datetime_tz_aware import DatetimeTzAwareField


class DatetimeFormatField(DatetimeTzAwareField):
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, *args, **kwargs):
        kwargs['format'] = self.DATE_FORMAT
        super(DatetimeFormatField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DatetimeFormatField, self).to_representation(value)
