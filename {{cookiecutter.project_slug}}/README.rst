{{ cookiecutter.project_slug }}
==========================================

Introduction

Usage, etc.


Local setup
-----------

These instructions assume that ``git``, ``docker``, and ``docker-compose`` are
installed on your host machine. For server provisioning and deployment,
``ansible`` is required as well.

This project makes use of Pipenv. If you are new to pipenv, install it and
study the output of ``pipenv --help``, especially the commands ``pipenv lock``
and ``pipenv sync``. Or read the `docs <https://docs.pipenv.org/>`_.

If this project depends on private packages, we will need to setup some authentication.
We do this using a `Personal access token <https://github.com/settings/tokens>`_. Generate one and
put it in your `$HOME/.netrc` file, as follows::

    machine github.com
    login <github username>
    password <github token>

    machine packages.lizard.net
    login nens
    password <packages.lizard.net password (check the internalpackages repo)>

For security reasons, make it readable only by you::

    $ chmod 600 ~/.netrc

The docker-compose file expects the following folders to exist:

 - ``~/.cache/pip``
 - ``~/.cache/pipenv``

Check if they exist and if you are the owner. If they do not exist, create them
with ``mkdir``, and if they are not owned by you, use ``sudo chown``.

Local development
-----------------

First, clone this repo and make some required directories::

    $ git clone git@github.com:nens/{{ cookiecutter.project_slug }}.git
    $ cd {{ cookiecutter.project_slug }}
    $ mkdir -p var/static var/media var/log

Then build the docker image, providing your user and group ids for correct file
permissions::

    $ docker-compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web

The entrypoint into the docker is set to `pipenv run`, so that every command is
executed in the pipenv-managed virtual environment. On the first `docker-compose run`,
the `.venv` folder will be created automatically inside your project directory::

    $ docker-compose run --rm web bash

If you happened to have created the virtual environment while outside the
docker, recreate it inside the docker. Optionally, add the `--site-packages` switch
to be able to import python packages that you installed with apt inside the
docker (e.g. mapnik)::

    (docker) $ pipenv --python 3.6 [--site-packages]

Then install the packages (including dev packages) listed in `Pipfile.lock`::

    (docker) $ pipenv sync --dev

Run migrations::

    (docker) $ python manage.py migrate

Then exit the docker shell (Ctrl + D)

At this point, you may want to test your installation::

    $ docker-compose run --rm web python manage.py test

Or start working with {{ cookiecutter.project_slug }} right away::

    $ docker-compose up

Now that Django is up and running, you may want to access the website from the
browser on your host machine. For this, you will need to open a port by generating
a local ``{{ cookiecutter.package_name }}/docker-compose.override.yml``. Checkout
``{{ cookiecutter.package_name }}/docker-compose.yml`` for an example.

To stop all running containers without removing them, do this::

    $ docker-compose stop

To update package versions (taking into account constraints in ``Pipfile``)::

    $ docker-compose run --rm web pipenv lock

And commit the newly generated ``Pipfile.lock``. If you make any change to
``Pipfile`` or ``setup.py``, you have to regenerate the lockfile.


Installation on the server
--------------------------

The ansible config and playbook is in the ``ansible/``
subdir. ``ansible/staging_inventory`` and ``ansible/production_inventory`` are
the two inventory files. Adjust variables (server name and gunicorn port)
in there.

The ``ansible/provision.yml`` playbook does the root-level stuff like
installing debian packages and creating a ``/srv/*`` directory. You should
only need to run this when there is a new debian dependency. It
also adds a couple of persons' ssh key to the ``~/.ssh/authorized_keys`` file
of the buildout user, which the deploy script uses to log you in directly as
user buildout.

The ``ansible/deploy.yml`` playbook is for the regular releases including git
checkout, pipenv sync, migration and supervisor restart.

Deploy command::

  $ ansible-playbook -i ansible/staging_inventory ansible/deploy.yml

If you don't have an ssh key set up, add ``-k`` to log in.

Provision command::

  $ ansible-playbook -K -i ansible/staging_inventory ansible/provision.yml


Development outside the Docker
-----------------------

If you have the same OS on your local machine as used in the ``Dockerfile``, you
may want to run your webserver outside a docker. You will need to install pipenv
on your machine (note the pinning because of
https://github.com/pypa/pipenv/issues/2666)::

    $ pip install --upgrade setuptools
    $ pip install pip==10.0.1 pipenv==2018.5.18

Also, make sure you have the debian packages as specified in the ``Dockerfile``.

Open up a port to the (still dockerized) db by adding a ``{{ cookiecutter.package_name }}/docker-compose.override.yml`` file.
Checkout  ``{{ cookiecutter.package_name }}/docker-compose.yml`` for an example.

Also, setup the same port in your local django settings
``{{ cookiecutter.package_name }}/localsettings.py``, as follows:

.. code-block:: python

    DATABASES['default']['HOST'] = 'localhost'
    DATABASES['default']['PORT'] = '5435'  # match this one with your docker-compose.override.yml

Then run the following commands::

    $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
    $ pipenv sync --dev
    $ docker-compose up db
    $ pipenv run python manage.py migrate
    $ pipenv run python manage.py runserver 0.0.0.0:5000
