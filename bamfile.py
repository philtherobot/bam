
from bam import *
from bam.cpp import *

project = Project()

lib = Library('phil_cpp')
lib.add(['source1.cpp', 'source2.cpp'])

project.add(lib)

exe = Executable('test')
exe.add(['test.cpp',lib])

project.add(exe)

print_tree(project)
