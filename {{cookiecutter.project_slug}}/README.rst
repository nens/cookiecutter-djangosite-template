{{ cookiecutter.project_slug }}
==========================================

Introduction

Usage, etc.


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

  $ ansible-playbook --inventory ansible/staging_inventory ansible/deploy.yml

Only needed for the initial install or when the nginx config has been changed
and so::

  $ ansible-playbook --inventory ansible/staging_inventory ansible/provision.yml

If you don't have an ssh key set up, add ``-k`` to log in. ``-K`` asks for a
sudo password if it isn't set up as passwordless.


Development with Docker
-----------------------

There's a docker file to make it easy for you to get started with the project
and to run the tests. You can edit files in the current directory and they'll
be picked up by docker right away.

The docker setup is also used by ``Jenkinsfile``, which means that our jenkins
instance will automatically pick it up.

First-time usage::

    $ ln -s development.cfg buildout.cfg
    $ docker-compose build
    $ docker-compose run --rm web python3 bootstrap.py
    $ docker-compose run --rm web bin/buildout
    $ docker-compose run --rm web bin/django migrate  # use '--fake-initial' if there are initial migrations
    $ docker-compose run --rm web bin/django createsuperuser
    $ docker-compose up

The site will now run on http://localhost:5000

Running the tests::

    $ docker-compose run --rm web bin/test

Note: on Linux the files generated in Docker will be owned by root. To fix this you
can run something like this inside your project directory::

    $ sudo chown -R $USER:$USER .

Adjust the list of ``.deb`` packages in Dockerfile if needed - and keep it in
sync with ``ansible/provision.yml``.
