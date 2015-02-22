
import bam.node as _node
import bam.sub_process as _subprocess
import bam.utils as _utils

import os.path as _path


class Library(_node.Node):
    def __init__(self, name):
        super(Library, self).__init__(name)


class Executable(_node.Node):
    def __init__(self, name):
        super(Executable, self).__init__(name)

    def add(self, seq):
        for s in seq:
            if isinstance(s, str):
                self.children.append(self._auto_detect(s))
            else:
                self.children.append(s)

    def _auto_detect(self, s):
        e = _path.splitext(s)
        if e[1] in ['.cpp', '.cxx']:
            return Source(s)

    def build(self):
        opts = { 'objs': [], 'libs': [] }
        for c in self.children:
            c._visit_link_options(opts)

        objs = ' '.join(opts['objs'])
        libs = ' -l'.join(opts['libs'])

        _subprocess.call('g++ {} {} -o {}'.format(objs, libs, self.name))


class Source(_node.FileNode):
    def __init__(self, name):
        super(Source, self).__init__(name)
        e = _path.splitext(self.name)
        self.interm = e[0] + '.o'

    def is_outdated(self):
        if not _path.exists(self.interm): return True
        return _utils.is_newer_file(self.name, self.interm)

    def build(self):
        _subprocess.call('g++ -c -std=c++11 {} -o {}'.format(self.name, self.interm))
        
    def _visit_link_options(self, opts):
        opts['objs'].append(self.interm)
                        
