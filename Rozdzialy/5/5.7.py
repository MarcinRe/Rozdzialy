# -*- coding: utf-8 -*-
print"---------------4.17----------------"
print 'a' and 'b'
print '' and 'b'
print 'a' and 'b' and 'c'
print"---------------4.18----------------"
print 'a' or 'b'
print '' or 'b'
print '' or [] or {}
def sidefx():
    print "in sidefx()"
    return 1
print 'a' or sidefx()
print"---------------4.19----------------"
a = "first"
b = "second"
print 1 and a or b
print 0 and a or b
print"---------------4.20----------------"
a = ""
b = "second"
print 1 and a or b
print"---------------4.21----------------"
a = ""
b = "second"
print (1 and [a] or [b])[0]