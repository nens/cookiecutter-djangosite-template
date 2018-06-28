FROM ubuntu:xenial

MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

# The -l option is to fix a problem with large user IDs (e.g. 1235227245).
# https://forums.docker.com/t/run-adduser-seems-to-hang-with-large-uid/27371/3
# https://github.com/moby/moby/issues/5419
ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid nens && useradd -lm -u $uid -g $gid nens

RUN apt-get update && apt-get install -y \
    git \
    python3-dev \
    python3-pip \
    libpq-dev \
    locales \
    memcached \
    postgresql-client \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

RUN pip3 install --upgrade setuptools pip
RUN pip3 install pipenv

VOLUME /code
WORKDIR /code
