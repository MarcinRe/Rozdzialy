# -*- coding: utf-8 -*-
print"---------------6.3-----------------"
f=open("C:\Users\Public\Music\Sample Music\Kalimba.mp3","rb")
print f
print f.mode
print f.name
print"---------------6.4-----------------"
print f
print f.tell()
f.seek(-128,2)
print f.tell()
tagData=f.read(128)
print tagData
print f.tell()
print"---------------6.5-----------------"
print f.closed
f.close()
print f
print f.closed
#f.seek(0)
#f.tell()
#f.read()
f.close()
print"---------------6.6-----------------"
#try:
#    fsock = open(filename, "rb",0)
#    try:
#        fsock.seek(-128,2)
#        tagdata = fsock.read(128)
#    finally:
#        fsock.close()
#except IOError:
#    pass
print"---------------6.7-----------------"
logfile = open('test.log', 'w')
logfile.write('udany test')
logfile.close()
print open('test.log').read()
logfile = open('test.log', 'a')
logfile.write('linia 2')
logfile.close()
print open('test.log').read()
