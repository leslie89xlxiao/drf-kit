from rest_framework import serializers


class DynamicModelFieldSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        default_exclude = getattr(self.Meta, 'exclude', [])
        if kwargs.get('exclude') is not None:
            exclude = kwargs.pop('exclude')
            self._delta_exclude = [i for i in default_exclude if i not in exclude]
        else:
            exclude = default_exclude
            self._delta_exclude = []
        self.fields.pop('DataChange_LastTime', None)
        self.fields.pop('is_deleted', None)
        super(DynamicModelFieldSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if exclude is not None:
            for field in exclude:
                self.fields.pop(field, None)

    def get_field_names(self, declared_fields, info):
        fields = super(DynamicModelFieldSerializer, self)\
            .get_field_names(declared_fields, info)

        return list(fields) + self._delta_exclude
