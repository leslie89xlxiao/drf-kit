from django.db import models
from django.db.models import F


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def increment(self, attribute):
        if getattr(self, attribute) is None:
            setattr(self, attribute, 0)

        setattr(self, attribute, F(attribute) + 1)
        self.save(update_fields=[attribute])

    def decrement(self, attribute):
        if getattr(self, attribute) is None:
            setattr(self, attribute, 0)

        setattr(self, attribute, F(attribute) - 1)
        self.save(update_fields=[attribute])

    def update_attributes(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
        self.save(update_fields=kwargs.keys())
