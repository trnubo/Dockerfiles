#!/bin/sh

etcd_base=/web
vhost=$(echo $SERVICE_NAME | sed 's/web\///')

env | grep "^VHOST" | while read item
do
  key=$(echo $item | cut -d= -f1)
  etcd_key=$(echo $key | sed 's/VHOST_//' | tr '[:upper:]' '[:lower:]')
  value=$(eval echo \$$key)
  echo "Vhost: $vhost, Key: $key, Value: $value"
  echo etcdctl set $etcd_base/$vhost/$etcd_key "$value"
done
