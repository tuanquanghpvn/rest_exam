from apps.base.mappers import (PagingRequestSchema, PagingResponseSchema)
from apps.category.mappers import (CategorySchema, GetCategoryRequestSchema, PostCategoryRequestSchema,
                                   PutCategoryRequestSchema, DeleteCategoryRequestSchema)
from contracts.base import (LIMIT_NAME, OFFSET_NAME, SORT_NAME, COUNT_NAME, CURRENT_NAME, PREV_NAME, NEXT_NAME)
from contracts.category import (CATEGORY_ID, NAME, SLUG, GetCategoryRequest, PostCategoryRequest, PutCategoryRequest,
                                DeleteCategoryRequest)

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

TEST_CATEGORY_ID = 1
TEST_CATEGORY_NAME = 'Category name 1'
TEST_CATEGORY_SLUG = 'category-name-1'

TEST_CATEGORY = {
    CATEGORY_ID: TEST_CATEGORY_ID,
    NAME: TEST_CATEGORY_NAME,
    SLUG: TEST_CATEGORY_SLUG
}

TEST_CATEGORY_POST = {
    NAME: TEST_CATEGORY_NAME,
    SLUG: TEST_CATEGORY_SLUG
}

TEST_CATEGORY_PUT = {
    NAME: TEST_CATEGORY_NAME,
    SLUG: TEST_CATEGORY_SLUG
}


def _test_category(category, has_id=False, has_name=False, has_slug=False):
    assert category.id == (TEST_CATEGORY_ID if has_id else None)
    assert category.name == (TEST_CATEGORY_NAME if has_name else None)
    assert category.slug == (TEST_CATEGORY_SLUG if has_slug else None)


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


class TestCategorySchema(object):
    def test_load(self):
        actual, errors = CategorySchema().load(TEST_CATEGORY)
        assert actual == TEST_CATEGORY
        assert errors == {}


class TestGetCategorySchema(object):
    def test_load(self):
        request = dict(PAGING_REQUEST)
        actual, errors = GetCategoryRequestSchema().load(request)
        assert isinstance(actual, GetCategoryRequest)
        assert errors == {}


class TestPostCategorySchema(object):
    def test_load(self):
        expected = {
            NAME: TEST_CATEGORY_NAME,
            SLUG: TEST_CATEGORY_SLUG
        }
        actual, errors = PostCategoryRequestSchema().load(expected)
        assert isinstance(actual, PostCategoryRequest)
        assert errors == {}
        _test_category(category=actual, has_name=True, has_slug=True)


class TestPutCategorySchema(object):
    def test_load(self):
        expected = {
            CATEGORY_ID: TEST_CATEGORY_ID,
            NAME: TEST_CATEGORY_NAME,
            SLUG: TEST_CATEGORY_SLUG
        }
        actual, errors = PutCategoryRequestSchema().load(expected)
        assert isinstance(actual, PutCategoryRequest)
        assert errors == {}
        _test_category(category=actual, has_id=True, has_name=True, has_slug=True)


class TestDeleteCategorySchema(object):
    def test_load(self):
        expected = {
            CATEGORY_ID: TEST_CATEGORY_ID,
        }
        actual, errors = DeleteCategoryRequestSchema().load(expected)
        assert isinstance(actual, DeleteCategoryRequest)
        assert errors == {}
        _test_category(category=actual, has_id=True)
