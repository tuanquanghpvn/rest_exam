from apps.category.tests.test_mappers import (TEST_CATEGORY_ID, TEST_CATEGORY_NAME, TEST_CATEGORY_SLUG)
from fixtures.factories.category import (CategoryFactory)
import pytest


@pytest.fixture
def create_category():
    CategoryFactory(id=TEST_CATEGORY_ID, name=TEST_CATEGORY_NAME, slug=TEST_CATEGORY_SLUG)

