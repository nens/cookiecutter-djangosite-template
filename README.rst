N&S django site cookiecutter template
=====================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh Django site project. It replaces the old "nensskel" tool.


Using this cookiecutter template
--------------------------------

Install/upgrade cookiecutter and pipenv::

  $ pip install cookiecutter pipenv --upgrade


Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-djangosite-template

Decide whether your project is an application or a library (`read more <https://docs.pipenv.org/advanced/#pipfile-vs-setuppy>`_ ).
For libraries, add ``Pipfile.lock`` to the newly generated ``.gitignore`` file.
For applications, generate a lockfile by running ``pipenv lock`` and commit the
generated ``Pipfile.lock``.

NB: If you require GDAL in your project, add ``pygdal`` as as dependency to the
``setup.py`` and pin ``pygdal`` in the ``Pipfile`` to a version that matches
the server OS version (for Ubuntu 16: 1.11.3) by calling::

  $ pipenv install pygdal==1.11.3.*


Development of this template itself
-----------------------------------

We don't need to run inside a vm/docker ourselves, so to set it up and test
it, just do the regular::

  $ pipenv install --dev
  $ pipenv run nosetests


The test, however, *does* use docker and docker-compose:

- There's a test that checks if the template itself generates OK without
  errors.

- There's a second test that uses the template-generated docker-compose setup
  to run the ``nosetests`` of the generated django.

We don't really need any python code ourselves, so our own ``setup.py``
doesn't actually point at any code. But it is set up so that ``nosetests``
finds and runs the tests inside ``./cookiecutter_tests/`` just fine.
