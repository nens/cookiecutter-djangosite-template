FROM ubuntu:xenial

MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

RUN apt-get update && apt-get install -y \
    git \
    python3-dev \
    python3-pip \
    libpq-dev \
    postgresql-client \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade setuptools pip
RUN pip3 install pipenv

VOLUME /code
WORKDIR /code
