import pytest

from zeus.django_asserts import dj_assert_template_used


@pytest.fixture
def report_resp(client):
    return client.get('/report/')


def test_report_status_code(report_resp):
    assert 200 == report_resp.status_code


def test_report_template_used(report_resp):
    dj_assert_template_used(report_resp, template_name='core/report.html')
