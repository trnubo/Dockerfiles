## Etcd to Docker links

This image creates Docker like links with data from 
[etcd](https://github.com/coreos/etcd) and 
[registrator](https://github.com/gliderlabs/registrator).

This is really a bit of a hack so we can get application that are not etcd or
service discovery aware working on a multi docker host environment. You should
look at a [ambassador patten](https://coreos.com/blog/docker-dynamic-ambassador-powered-by-etcd/) 
or make your application aware of service discovery directly.

## Usage

```
Usage: run.py [OPTIONS] [LINKS]...

  Main function

Options:
  --etcdctl-peers TEXT  ETCD peers list
  --services-base TEXT  Base path to services. Normally /services
  --name TEXT           Name of the container we're creating  [required]
  --output TEXT         Output environment file
  --maps TEXT
  --help                Show this message and exit.
```

### Limitations

Not all of the linked containers environment variables are exposed to the new
container like docker does on a single host.

Not quite enough information is recorded into etcd by registrator to match the
docker link environment variables but it should generally be sufficient.

Currently if there are multiples of the same service registered in etcd only
the first one will be saved into the environment.
