# -*- coding: utf-8 -*-
print"---------------4.22----------------"
def f(x):
    return x*2
print f(3)
g = lambda x: x*2
print g(3)
print (lambda x: x*2)(3)
print"---------------4.23----------------"
s="this    is\na\ttest"
print s
print s.split()
print " ".join(s.split())
