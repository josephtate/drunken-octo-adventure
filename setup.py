import os

try:
    os.mkdir('build')
except OSError, e:
    print str(e)

buildnum  = int(os.environ.get('BUILD_NUMBER', '9'))
os.system('touch build/drunken-octo-adventure-999-%00d.egg' % buildnum)
