# -*- coding: utf-8 -*-
print"---------------5.17---------------"
import fileinfo
print fileinfo.MP3FileInfo
print fileinfo.MP3FileInfo.tagDataMap
m=fileinfo.MP3FileInfo()
print m.tagDataMap
print"---------------5.18---------------"
class counter(object):
    count=0
    def __init__(self):
        self.__class__.count+=1

print counter
print counter.count
c=counter()
print c.count
print counter.count
d=counter()
print d.count
print c.count
print counter.count