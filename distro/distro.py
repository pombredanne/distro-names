# -*- coding: utf-8 -*-


"""distro.distro: provides entry point main()."""

__version__ = '0.0.1'

# TODO: Fix search for subterm, e.g. searching for '8' returns 8, 18, 28... Perhaps add "exact" matching for words...

import argparse

from distro.data import data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--output', type=str, default='text', help='Output format (text|json|csv)')
    ap.add_argument('search_term', nargs='*', help='Search terms, it can be a string or field:string')
    args = ap.parse_args()

    distros = load()
    results = search(args.search_term, distros)

    if args.output == 'text':
        display_text(results)
    elif args.output == 'json':
        display_json(results)
    elif args.output == 'csv':
        display_csv(results)


def load():
    return [Distro(**dt) for dt in data]


def search(terms, distros):
    results = []

    for d in distros:
        if all(t in d.raw() for t in terms):
            results.append(d)

    return results


def display_text(results):
    for r in results:
        print(r)


def display_csv(results):
    for r in results:
        print(r.raw())


def display_json(results):
    print('NOT IMPLEMENTED')
    for r in results:
        print(r.raw())


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
            if isinstance(v, list):
                s += '{}\n'.format(', '.join(v))
            else:
                s += '{}\n'.format(v)
        return s

    def raw(self):
        out = list()
        for k, v in sorted(self.data.items()):
            if isinstance(v, list):
                out.append('{}:{}'.format(k, ','.join(v)))
            else:
                out.append('{}:{}'.format(k, v))
        return ','.join(out).lower()
