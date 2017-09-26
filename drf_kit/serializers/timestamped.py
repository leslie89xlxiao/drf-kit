from rest_framework import serializers

from .fields import DatetimeFormatField


class TimestampedSerializer(serializers.ModelSerializer):
    created_at = DatetimeFormatField(read_only=True)
    updated_at = DatetimeFormatField(read_only=True)
