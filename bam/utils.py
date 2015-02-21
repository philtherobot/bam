from __future__ import print_function


def print_tree(p):
    _print_tree(p, 0)


def _print_tree(p, indent):
    i = ' ' * (indent * 2)
    print(i + p.name + ' ' + str(p))
    for c in p.children:
        _print_tree(c, indent+1)
