import os

from zeus.wsgi import application
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry


def test_wsgi_default_settings():
    assert 'zeus.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instace():
    assert isinstance(application, Sentry)
