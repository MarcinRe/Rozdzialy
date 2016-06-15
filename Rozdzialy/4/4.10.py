# -*- coding: utf-8 -*-
print"---------------3.34----------------"
errmsg=u'Nie można otowrzyć pliku'
print errmsg
print errmsg + u', brak dostępu.'
print errmsg.split()
print u"Błąd: %s" %errmsg
print"---------------3.35----------------"
file ='myfile.txt'
print errmsg + ' ' + file
print "%s %s"%(errmsg, file)
#print errmsg + ', brak dostępu.'
#print "Błąd: %s"%errmsg
print"---------------3.36----------------"
print errmsg.encode('iso-8859-2')
print errmsg.encode('utf-8')
print"---------------3.37----------------"
msg= errmsg.encode('utf-8')
msg.decode('utf-8')
print msg