# -*- coding: utf-8 -*-
print"---------------4.6-----------------"
li=[]
print type(1)
print type(li)
#import odbchelper
#type(odbchelper)
import types
#type(odbchelper) == types.ModuleType
print type(li)==types.ListType
print"---------------4.7-----------------"
print str(1)
horsemen =['war', 'pestilence','famine']
print horsemen
horsemen.append('Powerbuilder')
print str(horsemen)
print str(types)
print str(None)
print"---------------4.8-----------------"
import apihelper
print unicode(1)
print unicode(apihelper)
print unicode(horsemen[0])
#print unicode('jeździectwo')
print unicode ('jeździectwo','utf-8')
print"---------------4.9-----------------"
print dir(li)
d={}
print dir(d)
print"---------------4.10-----------------"
import string
print string.punctuation
print string.join
print callable(string.punctuation)
print callable(string.join)
print string.join.__doc__
print"---------------4.11-----------------"
from apihelper import info
import __builtin__
info(__builtin__,20)