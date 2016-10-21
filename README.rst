N&S django site cookiecutter template
=====================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh Django site project. It replaces the old "nensskel" tool.


Using this cookiecutter template
--------------------------------

Install cookiecutter ("pip install cookiecutter").

Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-djangosite-template


Development of this template itself
-----------------------------------

We don't need to run inside a vm/docker ourselves, so to set it up and test
it, just do the regular::

  $ python3 bootstrap.py
  $ bin/buildout
  $ bin/test

The test, however, *does* use docker and docker-compose:

- There's a test that checks if the template itself generates OK without
  errors.

- There's a second test that uses the template-generated docker-compose setup
  to run the ``bin/test`` of the generated django.

We don't really need any python code ourselves, so our own ``setup.py``
doesn't actually point at any code. But it is set up so that ``bin/test``
finds and runs the tests inside ``./cookiecutter_tests/`` just fine.
