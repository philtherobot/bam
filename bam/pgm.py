from __future__ import print_function

import sys

import bam.utils as _utils

class Pgm(object):
    def __init__(self, args):
        pass

    def execute(self):
        self.bamfile = {}
        execfile('bamfile', {}, self.bamfile)

        project = self.bamfile['project']
        #_utils.print_tree(project)

        project.explode()
        _utils.print_tree(project)

        project.build()
"""
g++ -std=c++11 -c hello.cpp -o hello.o
g++ hello.o -o hello
"""
        
def main():
    pgm = Pgm(sys.argv[1:])
    pgm.execute()


if __name__ == '__main__':
    main()
