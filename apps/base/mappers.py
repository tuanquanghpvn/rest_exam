from marshmallow import (Schema, fields, ValidationError)


def _check_include_fields(data, require_key, include_key):
    """Check loading field values.

    It's required or can be included in result.
    If it is invalid, raise error.
    This method should use in @validates_schema.

    :param dict data: input data
    :param list<str> require_key: Required key names
    :param list<str> include_key: Key names to include result
    :return:
    """
    error_msgs = []
    for key in require_key:
        if key not in data:
            error_msgs.append('Require field name: {}'.format(key))
    for key in data:
        if key not in include_key:
            error_msgs.append('Invalid field name: {}'.format(key))
    if len(error_msgs) > 0:
        raise ValidationError(error_msgs)


class PagingRequestSchema(Schema):
    limit = fields.Int(allow_none=True)
    offset = fields.Int(allow_none=True)
    sort = fields.Str(allow_none=True)


class PagingResponseSchema(Schema):
    count = fields.Int(allow_none=True)
    current = fields.Str(allow_none=True)
    prev = fields.Str(allow_none=True)
    next = fields.Str(allow_none=True)
