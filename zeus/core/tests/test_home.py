import pytest
from django.shortcuts import resolve_url as r
from zeus.django_asserts import dj_assert_template_used, dj_assert_contains


@pytest.fixture
def home_resp(client):
    return client.get('/')


def test_home_status_code(home_resp):
    assert 200 == home_resp.status_code


def test_home_use_template(home_resp):
    dj_assert_template_used(home_resp, template_name='core/index.html')


def test_home_contains_reports_link(home_resp):
    expected = f'href="{r("reports")}"'
    dj_assert_contains(home_resp, expected)
