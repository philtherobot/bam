
import bam as _bam


class Library(_bam.Node):
    def __init__(self, name):
        super(Library, self).__init__(name)


class Executable(_bam.Node):
    def __init__(self, name):
        super(Executable, self).__init__(name)
