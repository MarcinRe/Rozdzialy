# -*- coding: utf-8 -*-
print"---------------3.4-----------------"
d={"server":"mpilgrim","database":"master"}
print d
print d["server"]
print d["database"]
#print d["mpilgrim"]


print"---------------3.5-----------------"
print d
d["database"]="pubs"
print d
d["uid"]="sa"
print d

print"---------------3.6-----------------"
d={}
d["klucz"]="wartość"
d["klucz"]="inna wartość"
print d
d["Klucz"]="jeszcze inna wartość"
print d

print"---------------3.7-----------------"
d={'bazadanych':'pubs','serwer':'mpilgrim','uid':'sa'}
d["licznik"]=3
print d
d[42]="douglas"
print d

print"---------------3.8-----------------"
del d[42]
print d
d.clear()
print d