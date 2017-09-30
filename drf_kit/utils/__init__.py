def str2bool(value):
    if isinstance(value, bool):
        return value
    else:
        if isinstance(value, (str, basestring)):
            value = value.lower()
        return {'true': True, 'false': False}.get(value, False)
