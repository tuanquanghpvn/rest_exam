from marshmallow import Schema, fields, post_load, validates_schema, ValidationError
from contracts.category import PostCategoryRequest


def _non_blank(value):
    if len(value.strip()) <= 0:
        raise ValidationError('Field cannot be blank')


def _validate_slug(value):
    pass


class CategoryRequestSchema(Schema):
    name = fields.Str()
    slug = fields.Str(allow_none=False, validate=_validate_slug)


class PostCategoryRequestSchema(CategoryRequestSchema):
    @post_load
    def make_contract(self, data):
        return PostCategoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        pass


d = {
    "name": "vuong",
    "slug": "v-uon-v"
}
schema = PostCategoryRequestSchema()
obj, errors = schema.load(d)
