from rest_framework import serializers


class DatetimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        if isinstance(value, basestring):
            return value
        else:
            return super(DatetimeTzAwareField, self).to_representation(value)


class TimestampedSerializer(serializers.ModelSerializer):
    created_at = DatetimeTzAwareField(read_only=True)
    updated_at = DatetimeTzAwareField(read_only=True)
