N&S django site cookiecutter template
=====================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh Django site project. It replaces the old "nensskel" tool.


Using this cookiecutter template
--------------------------------

Install/upgrade cookiecutter::

  $ pip install --upgrade --user cookiecutter


Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-djangosite-template

Optionally add dependencies to the ``setup.py``. Then follow the installation
instructions inside the newly generated repository.

If you require matplotlib in your project:

 - uncomment ``libfreetype6-dev`` in both ``ansible/provision.yml`` and ``Dockerfile``
 - add ``matplotlib`` to your ``setup.py``


If you require GDAL in your project:

 - uncomment ``libgdal-dev`` in both ``ansible/provision.yml`` and ``Dockerfile``
 - do not add ``gdal`` as a dependency to the ``setup.py``
 - never import gdal with ``import gdal``, use ``from osgeo import gdal`` instead
 - pin ``pygdal`` in the ``Pipfile`` to a version that matches
   the server OS version (Ubuntu 16: 1.11.3; Ubuntu 18: 2.2.3) by calling::

  $ pipenv install pygdal==2.2.3.*


If you require mapnik in your project:

 - add ``python3-mapnik`` to the apt install in ``ansible/provision.yml`` and in ``Dockerfile``
 - do not add ``mapnik`` as a dependency to the ``setup.py``
 - initialize the pipenv with ``pipenv --site-packages`` (see project README)


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
