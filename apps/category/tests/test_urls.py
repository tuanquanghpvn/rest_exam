from rest_framework import status
from apps.category.tests.test_mappers import (TEST_CATEGORY_POST, TEST_CATEGORY_PUT, TEST_CATEGORY_ID, TEST_CATEGORY_NAME, TEST_CATEGORY_SLUG,
                                              CATEGORY_ID, NAME, SLUG)
import pytest
import json


@pytest.mark.integrationtest
class TestIntegration(object):
    @pytest.mark.usefixtures('create_category')
    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_get_category(self, client):
        get_result = client.get('/category/')
        assert get_result.status_code == status.HTTP_200_OK

    @pytest.mark.usefixtures('create_category')
    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_detail_category(self, client):
        get_result = client.get('/category/' + str(TEST_CATEGORY_ID) + '/')
        assert get_result.status_code == status.HTTP_200_OK
        assert get_result.data[NAME] == TEST_CATEGORY_NAME
        assert get_result.data[SLUG] == TEST_CATEGORY_SLUG

    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_post_category(self, client):
        get_result = client.post('/category/', data=json.dumps(TEST_CATEGORY_POST), content_type='application/json')
        assert get_result.status_code == status.HTTP_201_CREATED
        assert get_result.data[NAME] == TEST_CATEGORY_NAME
        assert get_result.data[SLUG] == TEST_CATEGORY_SLUG

    @pytest.mark.usefixtures('create_category')
    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_put_category(self, client):
        get_result = client.put('/category/' + str(TEST_CATEGORY_ID) + '/', data=json.dumps(TEST_CATEGORY_PUT),
                                content_type='application/json')
        assert get_result.status_code == status.HTTP_200_OK
        assert get_result.data[NAME] == TEST_CATEGORY_NAME
        assert get_result.data[SLUG] == TEST_CATEGORY_SLUG

    @pytest.mark.usefixtures('create_category')
    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_delete_category(self, client):
        get_result = client.delete('/category/' + str(TEST_CATEGORY_ID) + '/')
        assert get_result.status_code == status.HTTP_204_NO_CONTENT




