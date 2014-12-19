import os

try:
    os.mkdir('build')
except OSError, e:
    print str(e)

buildnum  = os.environ.get('BUILD_NUM', 9)
os.system('touch build/drunken-octo-adventure-999-%00d.egg' % buildnum)
