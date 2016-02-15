from marshmallow import (Schema, fields, post_load, validates_schema, ValidationError)
from contracts.story import (PostStoryRequest, PutStoryRequest, DeleteStoryRequest)
from contracts.story import (ID, ID_CATEGORY, NAME, SLUG, DESCRIPTION, CONTENT)


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
            error_msgs.append('Require field name {}'.format(key))
    for key in data:
        if key not in include_key:
            error_msgs.append('Invalid field name {}'.format(key))
    if len(error_msgs) > 0:
        raise ValidationError(error_msgs)


# Request

class StorySchema(Schema):
    id = fields.Int()
    category = fields.Int()
    name = fields.Str()
    slug = fields.Str()
    description = fields.Str(allow_none=True)
    content = fields.Str()


class PostCategoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return PostStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [ID_CATEGORY, NAME, SLUG, CONTENT]
        include_key = [ID_CATEGORY, NAME, SLUG, DESCRIPTION, CONTENT]
        _check_include_fields(data, require_key, include_key)


class PutCategoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return PutStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [ID]
        include_key = [ID, NAME, SLUG, DESCRIPTION, CONTENT]
        _check_include_fields(data, require_key, include_key)


class DeleteCategorySchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return DeleteStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [ID]
        include_key = []
        _check_include_fields(data, require_key, include_key)

# Response
