FROM ubuntu:xenial

MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

# Change the date to force rebuilding the whole image
ENV REFRESHED_AT 1972-12-25

# system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3-dev \
    python-pip \
    python3-psycopg2 \
    supervisor \
    gettext \
    postgresql-client \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/*

VOLUME /code
WORKDIR /code
