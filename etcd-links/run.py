#!/usr/bin/env python

import click
import sys
import os
from urlparse import urlparse
from etcd import Client, EtcdKeyNotFound
from pprint import pformat

@click.command()
@click.option('--etcdctl-peers', default='http://127.0.0.1:4001', help="ETCD peers list", envvar='ETCDCTL_PEERS')
@click.option('--services-base', default='/services', help="Base path to services. Normally /services")
@click.option('--name', required=True, help="Name of the container we're creating")
@click.option('--output', default='/output/environment', help="Output environment file")
@click.option('--maps', multiple=True)
@click.argument('links', nargs=-1)
def run(etcdctl_peers, services_base, name, output, maps, links):
    """Main function"""

    click.secho("Connecting to ECTD: %s" % etcdctl_peers, fg='green')

    click.secho("Links: %s" % " ".join(str(i) for i in links), fg='green')

    if len(links) == 0:
        click.echo("Nothing to do")
        sys.exit()

    etcd_url = urlparse(etcdctl_peers)
    etcd = Client(host=etcd_url.hostname, port=etcd_url.port)

    environment = {}

    # Get values from etcd for the services specified
    # --link <name or id>:alias
    for link in links:
        lname, _, alias = link.partition(":")
        if not alias:
            alias = lname.replace('-', '_')

        try:
            # Try to get the service
            service = etcd.read(os.path.join(services_base, lname))
            # Expects the service to have some children
            if len(service._children) > 0:
                value = service._children[0]["value"]
                ip, _, port = value.partition(":")
                click.secho("Key: %s found" % lname, fg='green')

                environment["%s_NAME" % alias.upper()] = "/%s/%s" % (name, lname)
                environment["%s_PORT" % alias.upper()] = "tcp://%s" % value
                environment["%s_PORT_%s_TCP" % (alias.upper(), port)] = "tcp://%s" % value
                environment["%s_PORT_%s_TCP_PROTO" % (alias.upper(), port)] = "tcp"
                environment["%s_PORT_%s_TCP_PORT" % (alias.upper(), port)] = "%s" % port
                environment["%s_PORT_%s_TCP_ADDR" % (alias.upper(), port)] = "%s" % ip
        except EtcdKeyNotFound:
            click.secho("Service: %s not found" % lname, fg='red')

    # Do mapping
    for item in maps:
        mname, _, alias = item.partition(":")
        if mname and alias:
            try:
                environment[alias] = environment[mname]
            except KeyError:
                click.secho("Missing Key: %s" % mname, fg='red')

    with open(output, 'w') as f:
        for key, value in environment.iteritems():
            f.write("%s=%s\n" % (key, value))
            click.secho("%s=%s" % (key, value), fg='yellow')

    click.secho("All done.", fg='green')

if __name__ == '__main__':
    run()
