import pytest

from zeus.django_asserts import dj_assert_template_used


@pytest.fixture
def home_resp(client):
    return client.get('/')


def test_home_status_code(home_resp):
    assert 200 == home_resp.status_code


def test_home_use_template():
    dj_assert_template_used(template_name='core/index.html')
