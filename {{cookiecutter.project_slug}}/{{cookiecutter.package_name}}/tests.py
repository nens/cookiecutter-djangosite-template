# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.test import TestCase
from {{ cookiecutter.package_name }} import admin
from {{ cookiecutter.package_name }} import models
from {{ cookiecutter.package_name }} import urls
from {{ cookiecutter.package_name }} import views


class ExampleTest(TestCase):

    def test_something(self):
        self.assertEquals(1, 1)
