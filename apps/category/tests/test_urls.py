from rest_framework import status
import pytest


@pytest.mark.integrationtest
class TestIntegration(object):
    @pytest.mark.usefixtures('create_category')
    @pytest.mark.django_db
    @pytest.mark.urls('rest_exam.urls')
    def test_get_category(self, client):
        get_result = client.get('/category/')
        assert get_result.status_code == status.HTTP_200_OK
