import os

try:
    os.mkdir('build')
except OSError, e:
    print str(e)

os.system('touch build/drunken-octo-adventure-999.egg')
