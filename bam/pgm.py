
import sys

import bam.utils as _utils
import bam.outdated as _outdated
import bam.build as _build


class Pgm(object):
    def __init__(self, args):
        pass

    def execute(self):
        self.bamfile = {}
        _utils.exec_file('bamfile', {}, self.bamfile)

        project = self.bamfile['project']
        #_utils.print_tree(project)

        #project.explode()

        outdated = _outdated.find(project)
        #for o in outdated: print(o)
        
        _build.run(outdated)

        
def main():
    pgm = Pgm(sys.argv[1:])
    pgm.execute()


if __name__ == '__main__':
    main()
