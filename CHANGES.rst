Changelog for cookiecutter-djangosite-template
==============================================


1.2 (unreleased)
----------------

- Updated jenkins setup: new workspace location means we need a setting to
  differentiate branches.

- Updated buildout setup: no more bootstrap, but a globally installed
  buildout.


1.1 (2017-08-25)
----------------

- Small fixes (unpinned setuptools, added gdal).


1.0 (2017-05-05)
----------------

- Improved coverage setup.

- Better Jenkinsfile (including docker-compose cleanup and coverage
  reporting).


0.1 (2017-03-13)
----------------

- Started project.

- Got first version of the template to work.

- Added docker test setup, Jenkins file and ansible integration.

- Fixed template configuration for recent django versions.
