from django.db import models
from django.db.models import F


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def increment(self, attribute):
        assert isinstance(attribute, int)

        attribute = F(attribute) + 1
        setattr(self, attribute)
        self.save()

    def update_attributes(self, **kwargs):
        for attribute, value in enumerate(kwargs):
            setattr(self, attribute)
        self.save()
