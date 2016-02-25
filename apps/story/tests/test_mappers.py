from apps.base.mappers import (PagingRequestSchema, PagingResponseSchema)
from apps.story.mappers import (StorySchema, GetStoryRequestSchema, PostStoryRequestSchema,
                                PutStoryRequestSchema, DeleteStoryRequestSchema)
from contracts.base import (LIMIT_NAME, OFFSET_NAME, SORT_NAME, COUNT_NAME, CURRENT_NAME, PREV_NAME, NEXT_NAME)
from contracts.story import (STORY_ID, NAME, SLUG, DESCRIPTION, CONTENT, CATEGORY_ID, GetStoryRequest, PostStoryRequest,
                             PutStoryRequest,
                             DeleteStoryRequest)

TEST_COUNT = 10
TEST_CURRENT = "http://sample"
TEST_PREV = "http://sample/prev"
TEST_NEXT = "http://sample/next"
TEST_LIMIT = 10
TEST_OFFSET = 10
TEST_SORT = "sort"
TEST_PATH = "http://sample/path"

PAGING_REQUEST = {
    LIMIT_NAME: TEST_LIMIT,
    OFFSET_NAME: TEST_OFFSET,
    SORT_NAME: TEST_SORT
}
PAGING_RESPONSE = {
    COUNT_NAME: TEST_COUNT,
    CURRENT_NAME: TEST_CURRENT,
    PREV_NAME: TEST_PREV,
    NEXT_NAME: TEST_NEXT
}

TEST_STORY_ID = 1
TEST_STORY_NAME = 'Story name 1'
TEST_STORY_SLUG = 'story-name-1'
TEST_STORY_DESCRIPTION = 'story description'
TEST_STORY_CONTENT = 'story content'
TEST_STORY_CATEGORY_ID = 1
TEST_STORY = {
    STORY_ID: TEST_STORY_ID,
    NAME: TEST_STORY_NAME,
    SLUG: TEST_STORY_SLUG,
    DESCRIPTION: TEST_STORY_DESCRIPTION,
    CONTENT: TEST_STORY_CONTENT,
    CATEGORY_ID: TEST_STORY_CATEGORY_ID
}

TEST_CATEGORY_POST = {
    NAME: TEST_STORY_NAME,
    SLUG: TEST_STORY_SLUG,
    DESCRIPTION: TEST_STORY_DESCRIPTION,
    CONTENT: TEST_STORY_CONTENT,
    CATEGORY_ID: TEST_STORY_CATEGORY_ID
}

TEST_CATEGORY_PUT = {
    NAME: TEST_STORY_NAME,
    SLUG: TEST_STORY_SLUG,
    DESCRIPTION: TEST_STORY_DESCRIPTION,
    CONTENT: TEST_STORY_CONTENT,
    CATEGORY_ID: TEST_STORY_CATEGORY_ID
}


def _test_story(story, has_id=False, has_name=False, has_slug=False, has_description=False,
                has_content=False, has_category_id=False):
    assert story.id == (TEST_STORY_ID if has_id else None)
    assert story.name == (TEST_STORY_NAME if has_name else None)
    assert story.slug == (TEST_STORY_SLUG if has_slug else None)
    assert story.description == (TEST_STORY_DESCRIPTION if has_description else None)
    assert story.content == (TEST_STORY_CONTENT if has_content else None)
    assert story.category_id == (TEST_STORY_CATEGORY_ID if has_category_id else None)


class TestPagingRequestSchema(object):
    def test_load(self):
        actual, errors = PagingRequestSchema().load(PAGING_REQUEST)
        assert actual == PAGING_REQUEST
        assert errors == {}


class TestPagingResponseSchema(object):
    def test_load(self):
        actual, errors = PagingResponseSchema().load(PAGING_RESPONSE)
        assert actual == PAGING_RESPONSE
        assert errors == {}


class TestStorySchema(object):
    def test_load(self):
        actual, errors = StorySchema().load(TEST_STORY)
        assert actual == TEST_STORY
        assert errors == {}


class TestGetStorySchema(object):
    def test_load(self):
        request = dict(PAGING_REQUEST)
        actual, errors = GetStoryRequestSchema().load(request)
        assert isinstance(actual, GetStoryRequest)
        assert errors == {}


class TestPostStorySchema(object):
    def test_load(self):
        expected = {
            NAME: TEST_STORY_NAME,
            SLUG: TEST_STORY_SLUG,
            DESCRIPTION: TEST_STORY_DESCRIPTION,
            CONTENT: TEST_STORY_CONTENT,
            CATEGORY_ID: TEST_STORY_CATEGORY_ID
        }
        actual, errors = PostStoryRequestSchema().load(expected)
        assert isinstance(actual, PostStoryRequest)
        assert errors == {}
        _test_story(story=actual, has_name=True, has_slug=True, has_content=True, has_category_id=True,
                    has_description=True)


class TestPutStorySchema(object):
    def test_load(self):
        expected = {
            STORY_ID: TEST_STORY_ID,
            NAME: TEST_STORY_NAME,
            SLUG: TEST_STORY_SLUG,
            DESCRIPTION: TEST_STORY_DESCRIPTION,
            CONTENT: TEST_STORY_CONTENT,
            CATEGORY_ID: TEST_STORY_CATEGORY_ID
        }
        actual, errors = PutStoryRequestSchema().load(expected)
        assert isinstance(actual, PutStoryRequest)
        assert errors == {}
        _test_story(story=actual, has_id=True, has_name=True, has_slug=True, has_content=True, has_category_id=True,
                    has_description=True)


class TestDeleteStorySchema(object):
    def test_load(self):
        expected = {
            STORY_ID: TEST_STORY_ID,
        }
        actual, errors = DeleteStoryRequestSchema().load(expected)
        assert isinstance(actual, DeleteStoryRequest)
        assert errors == {}
        _test_story(story=actual, has_id=True)
