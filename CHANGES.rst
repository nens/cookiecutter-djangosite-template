Changelog for cookiecutter-djangosite-template
==============================================


1.3 (unreleased)
----------------

- Set timezone to Europe/Amsterdam within Docker for consistency with our
  servers.

- Create the 'buildout' user with an unusable password. The name 'buildout'
  is for historical reasons and does not refer to the package manager used.

- Replaced buildout with pipenv as package manager.

- Updated Ubuntu version to 18 (and python to 3.6).

- Replaced Pep8 checking by Flake8 checking.

- Added the option to add celery.

- Generate a random SECRET_KEY.

- Enabled deployment without root privileges.


1.2 (2018-02-09)
----------------

- Updated jenkins setup: new workspace location means we need a setting to
  differentiate branches.

- Updated buildout setup: no more bootstrap, but a globally installed
  buildout.

- Updated urls.py to django 2.0.

- In development, a ``var/log/sql.log`` is created so that you can get a
  better feel for the number of queries.

- More modern Jenkinsfile:

    - Better project name, needed because of recent jenkins changes.

    - "Try/except" at the end so that docker cleanup is always done.

- Assuming python3.


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
