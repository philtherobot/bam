
class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    """
    def add(self, seq):
        if isinstance(seq, basestring):
            self._add_source(seq)
        else:
            try:
                for s in seq:
                    self.add(s)
            except TypeError:
                self.children.append(seq)
    """
    
    def build(self):
        for c in self.children:
            c.build()

    def explode(self):
        pass
        for c in self.children:
            c.explode()


class Project(Node):
    def __init__(self):
        super(Project, self).__init__('<project>')

    def add(self, seq):
        try:
            self.children += seq
        except TypeError:
            self.children.append(seq)
