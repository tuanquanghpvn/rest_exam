from marshmallow import (Schema, fields, post_load, validates_schema)
from contracts.story import (GetStoryRequest, GetStoryResponse,
                             DetailStoryRequest, DetailStoryResponse,
                             PostStoryRequest, PutStoryRequest, DeleteStoryRequest,
                             STORY_ID, CATEGORY_ID, NAME, SLUG, DESCRIPTION, CONTENT)
from apps.base.mappers import (_check_include_fields, PagingRequestSchema, PagingResponseSchema)


# Request

class StorySchema(Schema):
    id = fields.Int()
    category_id = fields.Int()
    name = fields.Str()
    slug = fields.Str()
    description = fields.Str(allow_none=True)
    content = fields.Str()


class GetStoryRequestSchema(PagingRequestSchema):
    category_id = fields.Int(allow_none=True)

    @post_load
    def make_contract(self, data):
        return GetStoryRequest(**data)


class DetailStoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return DetailStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [STORY_ID]
        include_key = [STORY_ID]
        _check_include_fields(data, require_key, include_key)


class PostStoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return PostStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [CATEGORY_ID, NAME, SLUG, CONTENT]
        include_key = [CATEGORY_ID, NAME, SLUG, DESCRIPTION, CONTENT]
        _check_include_fields(data, require_key, include_key)


class PutStoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return PutStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [STORY_ID]
        include_key = [STORY_ID, CATEGORY_ID, NAME, SLUG, DESCRIPTION, CONTENT]
        _check_include_fields(data, require_key, include_key)


class DeleteStoryRequestSchema(StorySchema):
    @post_load
    def make_contract(self, data):
        return DeleteStoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [STORY_ID]
        include_key = [STORY_ID]
        _check_include_fields(data, require_key, include_key)


# Response

class GetStoryResponseSchema(PagingResponseSchema):
    results = fields.Nested(StorySchema, many=True)


class DetailStoryResponseSchema(StorySchema):
    pass


class PostStoryResponseSchema(StorySchema):
    pass


class PutStoryResponseSchema(StorySchema):
    pass


class DeleteStoryResponseSchema(StorySchema):
    pass
