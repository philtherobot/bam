
import os as _os


def print_tree(p):
    _print_tree(p, 0)


def _print_tree(p, indent):
    i = ' ' * (indent * 2)
    print(i + p.name + ' ' + str(p))
    for c in p.children:
        _print_tree(c, indent+1)


def exec_file(fn, global_vars, local_vars):
    with open(fn) as f:
        code = compile(f.read(), fn, 'exec')
        exec(code, global_vars, local_vars)

def is_newer_file(a, b):
    return _os.stat(a).st_mtime > _os.stat(b).st_mtime
