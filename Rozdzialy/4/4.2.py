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
d36={}
d36["klucz"]="wartość"
d36["klucz"]="inna wartość"
print d36
d36["Klucz"]="jeszcze inna wartość"
print d36

print"---------------3.7-----------------"
d37={'bazadanych':'pubs','serwer':'mpilgrim','uid':'sa'}
d37["licznik"]=3
print d37
d37[42]="douglas"
print d37

print"---------------3.8-----------------"
del d37[42]
print d37
d37.clear()
print d37