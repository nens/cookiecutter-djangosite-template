# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
from django.test import TestCase
from {{ cookiecutter.package_name }} import admin
from {{ cookiecutter.package_name }} import models
from {{ cookiecutter.package_name }} import urls
from {{ cookiecutter.package_name }} import views


class ExampleTest(TestCase):
    def test_something(self):
        self.assertEquals(1, 1)
