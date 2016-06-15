# -*- coding: utf-8 -*-
print"---------------4.24----------------"
import apihelper
object=apihelper
method="info"
print getattr(object,method)
print getattr(object,method).__doc__
print"---------------4.25----------------"
def foo():
    print 2
foo()
print foo.__doc__
print foo.__doc__==None
print unicode(foo.__doc__)
print"---------------4.26----------------"
s='buildConnectionString'
print s.ljust(30)+'.'
print s.ljust(20)+'.'
print"---------------4.27----------------"
li = ['a','b','c']
print "\n".join(li)

