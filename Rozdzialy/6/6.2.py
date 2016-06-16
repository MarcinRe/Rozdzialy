# -*- coding: utf-8 -*-
print"---------------5.3-----------------"
class Nicosc(object):
    pass

print"---------------5.4-----------------"
#class FileInfo(dict):
print"---------------5.5-6---------------"
class FileInfo(dict):
    u"przechowuje metadane pliku"
    def __init__(self,filename=None):
        dict.__init__(self)
        self["plik"]=filename

