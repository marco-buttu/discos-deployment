#! /usr/bin/env python
"""Some command line examples:

  $ ./make discos_srt:development
  $ ./make discos_srt:production
  $ ./make discos_medicina:development
  $ ./make manager:development --station SRT
  $ ./make discos_srt:development --version 0.6
  $ ./make discos_srt:development --version latest
  $ ./make discos_srt:development --only deploying --version latest
  $ ./make discos_srt:development --only deploying --version master
  $ ./make discos_srt:development --only provisioning
"""

from __future__ import print_function
import os
import sys
import argparse
import itertools
import subprocess


ENVIRONMENTS = ['development', 'production']
STATIONS = {
    'SRT': 'discos_srt',
    'Medicina': 'discos_medicina',
    'Noto': 'discos_noto'
}
TAGS = ['provisioning', 'deploying']
REPO = 'https://github.com/marco-buttu/pycon_doctest.git'
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
ANSIBLE_DIR = os.path.join(ROOT_DIR, 'ansible')

systems = []
clusters = {}
all_clusters = []
for env in ENVIRONMENTS:
    clusters[env] = []
    inventory = '%s/inventories/%s' % (ANSIBLE_DIR, env)
    hosts_file = os.path.join(inventory, 'hosts')
    with open(hosts_file) as f:
        for line in f:
            if line.startswith('['):
                text = line[line.find('[')+1:line.find(']')]
                host = text.split(':')[0] if ':' in text else text
                if host not in  ('multi', 'local'):
                    all_clusters.append(host)
                    clusters[env].append(host)
                    systems.append('%s:%s' % (host, env))


parser = argparse.ArgumentParser(
    description='Make a disco environment. %s' % __doc__,
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(
    'system',
    help='%s, %s, ...' % (systems[-1], systems[-2]))
parser.add_argument(
    '-s',
    '--station',
    choices=STATIONS.keys(),
    default=None)
parser.add_argument(
    '-o',
    '--only',
    choices=TAGS,
    default=None)
parser.add_argument(
    '--sim',
    action='store_true',
    help='simulation mode')


def error(msg, choices=(), name=''):
    if choices:
        choices_msg = 'Allowed values of %s:\n' % name
    else:
        choices_msg = ''
    print('\nERROR: %s%s' % (msg, choices_msg), file=sys.stderr)
    if choices:
          for choice in choices:
              print(' '*2, choice, file=sys.stderr)
    print('\n%s' %  __doc__, file=sys.stderr)
    sys.exit(1)
args = parser.parse_args()


# Check if the system cluster:environment exists
if args.system.count(':') != 1:
    e = ENVIRONMENTS[-1]  # A random environment
    c = clusters[e][-1]  # A random cluster
    msg = ('You must specify an available system.\n'
           'e.g. if the cluster is "%s" '
           'and the environment is "%s",\n'
           'the system is "%s:%s", and the command will be:'
           '\n\n  $ ./make %s:%s.\n\n' % (c, e, c, e, c, e))
    error(msg, choices=systems, name='system')
else:
    cluster_arg, env_arg = args.system.split(':')
    if env_arg in ENVIRONMENTS:
        allowed_clusters = clusters[env_arg]
        c = allowed_clusters[-1]  # A random cluster
        # wrong_cluster:right_env
        if cluster_arg not in allowed_clusters:
            msg = ('Cluster "%s" not found in the "%s" '
                   'environment.\n' % (cluster_arg, env_arg))
            error(msg,
                  allowed_clusters,
                  name='cluster (in %s)' % env_arg)
    else:
        # right_cluster:wrong_env
        if cluster_arg in all_clusters:
            msg = ('Environment "%s" not found in %s.\n'
                   'Please use a right cluster:environment combination, like:\n'
                   '%s, %s, %s, ...'
                   % (env_arg, ENVIRONMENTS, systems[0], systems[-1], systems[-2]))
            error(msg)
        # wrong_cluster:wrong_env
        if cluster_arg not in all_clusters:
            error('System "%s:%s" not recognized.\n' % (cluster_arg, env_arg),
                  systems,
                  name='system')

inventory = '%s/inventories/%s' % (ANSIBLE_DIR, env_arg)

if cluster_arg in STATIONS.values():
    # When the system is discos_srt, discos-medicina or discos_noto,
    # the station is automatically set to SRT, Medicina, and Noto
    for station in STATIONS:
        if STATIONS[station] == cluster_arg:
            default_station = station
            break
    extra_vars = '"cdb=%s"' % default_station

if args.station is not None:
    # Override the default value
    extra_vars = '"cdb=%s"' % args.station

# Version management
# $ ./make discos_srt development --version 0.6
# Come posso gestire due versioni? Se voglio avere nella
# Stessa macchina il master e la versione X?
# Potrei fare cosi': quando uno da --version, allora
# viene usato il tag deploying e anche quello version. 
# Il tag version verifica se quella versione esiste gia',
# e se non esiste fa il clone e configura acsenv in modo
# da creare un alias che permetta di passare da una introot
# all'altra.  L'introot viene creata durante il deploying,
# non durante acs.yml.
# Il prompt della shell deve mostrare il tipo di branch:
# master, version-0.6, ecc.

playbook = '%s/all.yml'  % ANSIBLE_DIR
tags = ''

command = [
    'ansible-playbook', playbook,
    '--inventory-file', inventory,
    '--limit', cluster_arg,
    '--extra-vars', extra_vars,
    '--tags', tags
]

if args.sim:
    print('You want to call:')
    print(' '.join(command))

else:
    subprocess.call(command)
