# -*- coding: utf-8 -*-
print"---------------3.9-----------------"
li=["a","b","mpilgrim","z","przykład"]
print li
print li[0]
print li[4]
print"---------------3.10----------------"
print li[-1]
print li[-3]
print"---------------3.11----------------"
print li[1:3]
print li[1:-1]
print li[0:3]
print"---------------3.12----------------"
print li[:3]
print li[3:]
print li[:]
print"---------------3.13----------------"
li.append("nowy")
print li
li.insert(2,"nowy")
print li
li.extend(["dwa","elementy"])
print li
print"---------------3.14----------------"
li=['a','b','c']
li.extend(['d','e','f'])
print li
print len(li)
print li[-1]
li=['a','b','c']
li.append(['d','e','f'])
print len(li)
print li[-1]
print"---------------3.15----------------"
li=["a","b","nowy","mpilgrim","z","przykład","nowy","dwa","elementy"]
print li
print li.index("przykład")
print li.index("nowy")
#print li.index("c")
print ("c" in li)
print"---------------3.16----------------"
li.remove("z")
print li
li.remove("nowy")
print li
#li.remove("c")
#print li
li.pop()
print li
print"---------------3.17----------------"
li = ['a','b','mpilgrim']
li =li+['przykład','nowy']
print li
li+=['dwa']
print li
li=[1,2]*3
print li