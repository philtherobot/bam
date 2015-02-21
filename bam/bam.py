
class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, seq):
        if isinstance(seq, basestring):
            self._add_source(seq)
        else:
            try:
                for s in seq:
                    self.add(s)
            except TypeError:
                self.children.append(seq)

    def _add_source(self, src):
        self.children.append(Source(src))


class Source(Node):
    def __init__(self, name):
        super(Source, self).__init__(name)


class Project(Node):
    def __init__(self):
        super(Project, self).__init__('<project>')
