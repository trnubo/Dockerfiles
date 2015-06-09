FROM debian:jessie

MAINTAINER Tim Robinson <tim@panubo.com>

RUN useradd -s /bin/bash -U --uid 48 -c 'Toolbox User' user

RUN apt-get update && \
  apt-get install -y git tar bzip2 unzip zip lftp curl wget mariadb-client sudo

RUN echo "user	ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/user && \
  chmod 600 /etc/sudoers.d/user

USER user
