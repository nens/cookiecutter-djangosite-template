from cookiecutter.main import cookiecutter
from shutil import rmtree
from unittest import TestCase

import os
import subprocess
import tempfile


class BasicTest(TestCase):

    def setUp(self):
        self.our_dir = os.getcwd()
        # The next line makes sure the temp dir is generates in our current
        # directory instead of in /tmp. This is needed for using the egg cache
        # on the Jenkins server. You get a "invalid cross-device link" error
        # otherwise.
        tempfile.tempdir = self.our_dir
        self.temp_dir = tempfile.mkdtemp(suffix='cookiecuttertest')
        os.chdir(self.temp_dir)
        self.defaults = {
            "full_name": "Reinout van Rees",
            "email": "reinout@vanrees.org",
            "project_slug": "world-domination",
            "project_short_description": "Speaks for itself"
        }

    def tearDown(self):
        for possible_hardlink in ['eggs', 'downloads']:
            hardlink = os.path.join(self.temp_dir,
                                    'world-domination',
                                    possible_hardlink)
            if os.path.exists(hardlink):
                os.remove(hardlink)
                # This way we don't zap the full contents of these dirs:
                # they're meant as cache.
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
        os.link(os.path.join(self.our_dir, 'eggs'), 'eggs')
        os.link(os.path.join(self.our_dir, 'downloads'), 'downloads')
        exit_code = subprocess.call(['ln',
                                     '-s',
                                     'development.cfg',
                                     'buildout.cfg'])
        self.assertEquals(0, exit_code)
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
