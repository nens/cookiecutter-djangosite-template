{{ cookiecutter.project_slug }}
==========================================

Introduction

Usage, etc.


Local development
-----------------

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
    password <packages.lizard.net password>

For security reasons, make it readable only by you::

    $ chmod 600 ~/.netrc


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

    $ docker-compose run --rm bash

If this is a first time use, or if you want to bump package versions, generate
a (new) `Pipfile.lock`::

    $ pipenv lock

Then install the packages (including dev packages) listed in `Pipfile.lock`::

    $ pipenv sync --dev

Run migrations::

    $ python manage.py migrate

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

