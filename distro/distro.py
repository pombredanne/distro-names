# -*- coding: utf-8 -*-


"""distro.distro: provides entry point main()."""

__version__ = '0.0.1'

import sys

from distro.data import data


def main():
    distros = [Distro(**dt) for dt in data]
    print("OS Distro finder version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])

    for d in distros:
        print(d)


class Distro(object):
    def __init__(self, **kwargs):
        self.data = kwargs

        if 'name' not in self.data.keys():
            raise Exception('Name is required')
        if 'version' not in self.data.keys() and 'versions' not in self.data.keys():
            raise Exception('Either version or list of versions required')
        if 'flavour' not in self.data.keys():
            self.data['flavour'] = 'Linux'

        if self.data.get('versions', None) is None:
            self.data['versions'] = list()
        elif isinstance(self.data.get('versions', None), str):
            self.data['versions'] = list(self.data['versions'])

        v = self.data.pop('version', None)
        if v is not None and v not in self.data['versions']:
            self.data['versions'].append(v)

    def __str__(self):
        lpad = max([len(k) for k in self.data.keys()]) + 5
        s = ''
        for k, v in sorted(self.data.items()):
            s += '{}:'.format(k.replace('_', ' ').title()).ljust(lpad, ' ')
            s += '{}\n'.format(v)
        s += '\n'
        return s
