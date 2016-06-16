# -*- coding: utf-8 -*-
print"---------------6.8-----------------"
li=['a','b','e']
for s in li:
    print s
print "\n".join(li)
print"---------------6.9-----------------"
for i in range(5):
    print i
li=['a','b','c','d','e']
for i in range (len(li)):
    print li[i]
print"---------------6.10----------------"
import os
for k, v in os.environ.items():
    print "%s=%s" % (k, v)
print "\n".join(["%s=%s" % (k, v)
    for k, v in os.environ.items()])