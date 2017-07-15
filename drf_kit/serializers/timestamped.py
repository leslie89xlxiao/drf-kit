from rest_framework import serializers

from fields import DatetimeTzAwareField


class TimestampedSerializer(serializers.ModelSerializer):
    created_at = DatetimeTzAwareField(read_only=True)
    updated_at = DatetimeTzAwareField(read_only=True)
