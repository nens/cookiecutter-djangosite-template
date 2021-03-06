from cookiecutter.main import cookiecutter
from shutil import rmtree
from unittest import TestCase

import os
import tempfile


class BasicTest(TestCase):

    def setUp(self):
        self.our_dir = os.getcwd()
        self.temp_dir = tempfile.mkdtemp(suffix='cookiecuttertest')
        os.chdir(self.temp_dir)
        self.defaults = {
            "full_name": "Reinout van Rees",
            "email": "reinout@vanrees.org",
            "project_slug": "world-domination",
            "project_short_description": "Speaks for itself"
        }

    def tearDown(self):
        rmtree(self.temp_dir, ignore_errors=True)
        os.chdir(self.our_dir)

    def test_smoke(self):
        cookiecutter(self.our_dir,
                     no_input=True,
                     extra_context=self.defaults)
        self.assertIn('README.rst',
                      os.listdir(self.temp_dir + '/world-domination'))
