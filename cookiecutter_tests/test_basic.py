from cookiecutter.main import cookiecutter
from cookiecutter.utils import rmtree
from unittest import TestCase

import os
import subprocess
import tempfile


class BasicTest(TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(suffix='cookiecuttertest')
        self.our_dir = os.getcwd()
        os.chdir(self.temp_dir)
        self.defaults = {
            "full_name": "Reinout van Rees",
            "email": "reinout@vanrees.org",
            "project_slug": "world-domination",
            "project_short_description": "Speaks for itself"
        }

    def tearDown(self):
        rmtree(self.temp_dir)
        os.chdir(self.our_dir)

    def test_smoke(self):
        cookiecutter(self.our_dir,
                     no_input=True,
                     extra_context=self.defaults)
        self.assertIn('README.rst',
                      os.listdir(self.temp_dir + '/world-domination'))

    def test_django_tests_run(self):
        cookiecutter(self.our_dir,
                     no_input=True,
                     extra_context=self.defaults)
        os.chdir('world-domination')
        exit_code = subprocess.call(['docker-compose',
                                     'run',
                                     'web',
                                     'python3',
                                     'bootstrap.py'])
        self.assertEquals(0, exit_code)
        exit_code = subprocess.call(['docker-compose',
                                     'run',
                                     'web',
                                     'bin/buildout'])
        self.assertEquals(0, exit_code)
        exit_code = subprocess.call(['docker-compose',
                                     'run',
                                     'web',
                                     'bin/test'])
        self.assertEquals(0, exit_code)
