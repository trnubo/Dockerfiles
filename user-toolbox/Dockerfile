FROM debian:jessie

MAINTAINER Tim Robinson <tim@panubo.com>

RUN useradd -s /bin/bash -U --uid 48 -c 'Toolbox User' user

RUN apt-get update && \
  apt-get install -y git tar bzip2 unzip zip lftp curl wget mariadb-client sudo pv vim nano

RUN echo "user	ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/user && \
  chmod 600 /etc/sudoers.d/user

RUN apt-get -y update && \
  apt-get -y install curl wget vim && \
  curl -L  https://github.com/coreos/etcd/releases/download/v2.0.11/etcd-v2.0.11-linux-amd64.tar.gz -o etcd-v2.0.11-linux-amd64.tar.gz && \
  tar xzvf etcd-v2.0.11-linux-amd64.tar.gz && \
  cp -a etcd-v2.0.11-linux-amd64/etcd etcd-v2.0.11-linux-amd64/etcdctl /usr/local/bin

USER user
