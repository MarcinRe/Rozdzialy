# -*- coding: utf-8 -*-
print"---------------6.1-----------------"
#fsock=open("/niemapliku", "r")
try:
    fsock = open("c:/niemapliku.txt")
except IOError:
    print "Plik nie istnieje"
print "Ta linia zawsze zostanie wypisana"
print"---------------6.2-----------------"
try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass