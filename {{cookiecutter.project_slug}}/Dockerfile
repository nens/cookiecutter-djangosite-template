FROM ubuntu:bionic

MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

# Create a nens user and group, with IDs matching those of the developer.
# The default values can be overridden at build-time via:
#
# docker-compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web
#
# The -l option is to fix a problem with large user IDs (e.g. 1235227245).
# https://forums.docker.com/t/run-adduser-seems-to-hang-with-large-uid/27371/3
# https://github.com/moby/moby/issues/5419
ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid nens && useradd -lm -u $uid -g $gid nens

# Get rid of debconf messages like "unable to initialize frontend: Dialog".
# https://github.com/docker/docker/issues/4032#issuecomment-192327844
ARG DEBIAN_FRONTEND=noninteractive

# Note: The official Debian and Ubuntu images automatically run apt-get clean,
# so explicit invocation is not required. See RUN apt-get in "Best practices
# for writing Dockerfiles". https://docs.docker.com/engine/userguide/↵
# eng-image/dockerfile_best-practices/
#
# Installing GDAL python bindings via pipenv requires libgdal-dev.
#
# Curl and xz-utils are used to install Node.js, see below.
#
# Checking out repositories via mr.developer requires git. Git is also
# needed for releases via zest.releaser.
#
# Installing psycopg2 via pip requires libpq-dev. The latter is also a
# dependency of libgdal-dev, but explicit is better than implicit.
RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    # libgdal-dev \       uncomment if the project requires pygdal
    # libfreetype6-dev \  uncomment if the project requires matplotlib
    memcached \
    python3-dev \
    python3-pip \
    locales \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

# Note the pinning because of https://github.com/pypa/pipenv/issues/2666
RUN pip3 install --upgrade setuptools && pip3 install pip==10.0.1 pipenv==2018.5.18

VOLUME /code
WORKDIR /code
USER nens
