from rest_framework import serializers


class DatetimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        if isinstance(value, basestring):
            return value
        else:
            return super(DatetimeTzAwareField, self).to_representation(value)
