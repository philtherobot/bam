
class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def is_outdated(self):
        return False

    def build(self):
        pass

    def explode(self):
        pass


class Project(Node):
    def __init__(self):
        super(Project, self).__init__('<project>')

    def add(self, seq):
        try:
            self.children += seq
        except TypeError:
            self.children.append(seq)


class FileNode(Node):
    def __init__(self, name):
        super(FileNode, self).__init__(name)

    def is_outdated(self):
        return False
