{{ cookiecutter.project_slug }}
==========================================

Introduction

Usage, etc.


Development
-----------

This project makes use of `Pipenv <https://docs.pipenv.org/>`_, which creates
a project virtual environment. We like to keep this virtual environment inside
``{{ cookiecutter.project_slug }}/.venv``. This is not the default Pipenv
behaviour, so we need to set the following environment variable:
``export PIPENV_VENV_IN_PROJECT=1``. If you add that to your ``.bashrc``, you
don't need to specify it each time.

Install the environment::

    $ pipenv install --deploy --dev
    $ mkdir -p var/static var/media var/log

As we want to avoid port clashes, you have to open a port from your host to
the database inside your docker. You should specify "host:docker" port mappings
in  a local ``{{ cookiecutter.package_name }}/docker-compose.override.yml``,
as follows:

.. code-block:: yaml

    version: '3'
    services:

      db:
        ports:
          - "5435:5432"  # the first one should the one in the localsettings

Also, set the same port in your local django settings
``{{ cookiecutter.package_name }}/localsettings.py``, as follows:

.. code-block:: python

    DATABASES['default']['HOST'] = 'localhost'
    DATABASES['default']['PORT'] = '5435'  # match this one with the docker-compose file

Start the database::

    $ docker-compose up db

Migrate the database::

    $ pipenv run python manage.py migrate

Run the webserver using your favourite IDE, or from the commandline::

    $ pipenv run python manage.py runserver 0.0.0.0:5000


Installation on the server
--------------------------

The ansible config and playbook is in the ``ansible/``
subdir. ``ansible/staging_inventory`` and ``ansible/production_inventory`` are
the two inventory files. Adjust variables (like checkout name and server name)
in there.

The ``ansible/provision.yml`` playbook does the root-level stuff like
installing debian packages and creating a ``/srv/*`` directory. You should
only need to run this when there's a new debian dependency, for instance. It
also adds a couple of persons' ssh key to the ``~/.ssh/authorized_keys`` file
of the buildout user, which the deploy script uses to log you in directly as
user buildout.

The ``ansible/deploy.yml`` playbook is for the regular releases including git
checkout, bin/buildout, migration and supervisor restart.

General usage::

  $ ansible-playbook -i ansible/staging_inventory ansible/deploy.yml

Only needed for the initial install or when the nginx config has been changed
and so::

  $ ansible-playbook -i ansible/staging_inventory ansible/provision.yml

If you don't have an ssh key set up, add ``-k`` to log in. ``-K`` asks for a
sudo password if it isn't set up as passwordless.


Development with Docker
-----------------------

There's a docker file to make it easy for you to get started with the project
and to run the tests. You can edit files in the current directory and they'll
be picked up by docker right away.

The docker setup is also used by ``Jenkinsfile``, which means that our jenkins
instance will automatically pick it up.

As we want to avoid port clashes, you have to open a ports from your docker
webserver to your host system. You should specify "host:docker" port mappings in
a local ``{{ cookiecutter.package_name }}/docker-compose.override.yml``, as follows:

.. code-block:: yaml

    version: '3'
    services:

      db:
        ports:
          - "5000:8000"  # pick your favourite port for access from your local browser


First-time usage::

    $ export UID  # or add this to your .bashrc
    $ docker-compose build
    $ docker-compose run --rm web pipenv install --deploy --dev
    $ docker-compose run --rm web pipenv run python manage.py migrate
    $ docker-compose up

The site will now run on http://localhost:5000 (or whatever port you picked)

Running the tests::

    $ docker-compose run --rm web pipenv run python manage.py test

